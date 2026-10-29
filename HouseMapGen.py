"""ランダムな住宅間取りを透過PNGで生成（Pillow + tkinter）。"""
import random
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from collections import deque
from PIL import Image, ImageDraw, ImageTk

S = 200
WALL = 40
FLOOR = (202, 166, 113, 255)
WALL_COLOR = (65, 65, 68, 255)


class Generator:
    def __init__(self, w, h, rectangular=False):
        self.w, self.h = w, h
        self.rectangular = rectangular
        self.cells = {(x, y) for x in range(w) for y in range(h)}
        self.corridor = self._make_corridor()
        # 約半分の確率で外周の角を削り、L字・凹型の建物にする。
        if not self.rectangular and w >= 5 and h >= 5 and random.random() < .5:
            for _ in range(random.randint(1, 3)):
                cw = random.randint(1, max(1, w // 3))
                ch = random.randint(1, max(1, h // 3))
                x0 = random.choice((0, w - cw))
                y0 = random.choice((0, h - ch))
                cut = {(x, y) for x in range(x0, x0 + cw)
                       for y in range(y0, y0 + ch)}
                if not cut.intersection(self.corridor):
                    self.cells.difference_update(cut)
        self.rooms = self._make_rooms()
        self.doors = set()
        for room in self.rooms:
            candidates = [(p, q) for p in room for q in self._neighbors(p)
                          if q in self.corridor]
            if candidates:
                p, q = random.choice(candidates)
                self.doors.add(frozenset((p, q)))
        self.entrance = (self.entry_x, 0)

    def _neighbors(self, p):
        x, y = p
        return ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))

    def _make_corridor(self):
        """玄関から続く廊下を作り、枝道と接続路で分岐・合流を追加する。"""
        self.entry_x = random.randrange(1, self.w - 1) if self.w >= 4 else self.w // 2
        bend = random.randint(1, self.h - 2)
        corridor = {(self.entry_x, y) for y in range(bend + 1)}
        if self.w >= 4 and self.h >= 4 and random.random() < .75:
            ends = [x for x in range(1, self.w - 1) if abs(x - self.entry_x) >= 1]
            target = random.choice(ends) if ends else self.entry_x
            corridor.update((x, bend) for x in range(min(target, self.entry_x), max(target, self.entry_x) + 1))
            if random.random() < .55:
                corridor.update((target, y) for y in range(bend, self.h))
        else:
            corridor.update((self.entry_x, y) for y in range(bend, self.h))

        # 既存廊下から横枝を伸ばし、別の廊下へ接続することで合流路も作る。
        branch_count = max(1, min(8, (self.w * self.h) // 35))
        for _ in range(branch_count):
            anchors = list(corridor)
            ax, ay = random.choice(anchors)
            if self.w > 3 and random.random() < .75:
                target_x = random.randrange(self.w)
                lo, hi = sorted((ax, target_x))
                corridor.update((x, ay) for x in range(lo, hi + 1))
                # 半分程度は枝の先を縦に延ばし、既存廊下に接続してループを形成。
                if random.random() < .55:
                    target_y = random.randrange(self.h)
                    lo_y, hi_y = sorted((ay, target_y))
                    corridor.update((target_x, y) for y in range(lo_y, hi_y + 1))
            else:
                target_y = random.randrange(self.h)
                lo_y, hi_y = sorted((ay, target_y))
                corridor.update((ax, y) for y in range(lo_y, hi_y + 1))
        return corridor

    def _make_rooms(self):
        """全部屋の縦・横を最低2マスにする。基本は長方形。"""
        remaining = self.cells - self.corridor
        rooms = []

        def rectangle(x0, y0, x1, y1):
            return {(x, y) for x in range(x0, x1 + 1)
                    for y in range(y0, y1 + 1)}

        def touches_corridor(area):
            return any(q in self.corridor for p in area for q in self._neighbors(p))

        # まず2×2以上の長方形が収まる場所だけを候補にする。
        # 1マス幅の余りは無理に部屋にせず、透過領域として扱う。
        while True:
            candidates = []
            for x in range(self.w - 1):
                for y in range(self.h - 1):
                    block = rectangle(x, y, x + 1, y + 1)
                    if block <= remaining and touches_corridor(block):
                        candidates.append((x, y))
            if not candidates:
                break

            x0, y0 = random.choice(candidates)
            x1, y1 = x0 + 1, y0 + 1
            max_area = random.randint(4, max(4, min(24, self.w * self.h // 3)))
            for _ in range(self.w + self.h):
                options = []
                for nx0, ny0, nx1, ny1 in (
                    (x0 - 1, y0, x1, y1), (x0, y0 - 1, x1, y1),
                    (x0, y0, x1 + 1, y1), (x0, y0, x1, y1 + 1)
                ):
                    if nx0 < 0 or ny0 < 0 or nx1 >= self.w or ny1 >= self.h:
                        continue
                    area = rectangle(nx0, ny0, nx1, ny1)
                    if area <= remaining and len(area) <= max_area:
                        options.append((nx0, ny0, nx1, ny1))
                if not options:
                    break
                x0, y0, x1, y1 = random.choice(options)
            room = rectangle(x0, y0, x1, y1)
            rooms.append(room)
            remaining -= room

        # 通常モードでは部屋にならない余剰マスを透明にする。
        # 長方形モードでは余剰マスを隣接する部屋に取り込み、1×1の孤立した
        # 小部屋のように見える領域を作らない。建物外周の床は維持する。
        if not self.rectangular:
            self.cells.difference_update(remaining)
        else:
            unassigned = set(self.cells) - set(self.corridor)
            for room in rooms:
                unassigned.difference_update(room)

            # 既存の部屋に隣接する余剰マスを順次取り込む。
            # 取り込み先は隣接部屋のうちランダムに選び、自然な部屋形状を保つ。
            while unassigned:
                attachable = []
                for cell in unassigned:
                    adjacent = [i for i, room in enumerate(rooms)
                                if any(q in room for q in self._neighbors(cell))]
                    if adjacent:
                        attachable.append((cell, adjacent))
                if not attachable:
                    break
                random.shuffle(attachable)
                for cell, adjacent in attachable:
                    if cell not in unassigned:
                        continue
                    adjacent = [i for i in adjacent
                                if any(q in rooms[i] for q in self._neighbors(cell))]
                    if adjacent:
                        rooms[random.choice(adjacent)].add(cell)
                        unassigned.remove(cell)
            # 部屋に隣接しない余剰マスは廊下に取り込み、孤立した区画をなくす。
            self.corridor.update(unassigned)

        # 約10%の家で、2つの十分な大きさの部屋を統合して変形室にする。
        if len(rooms) >= 2 and random.random() < .10:
            pairs = [(i, j) for i in range(len(rooms)) for j in range(i + 1, len(rooms))
                     if any(q in rooms[j] for p in rooms[i] for q in self._neighbors(p))]
            random.shuffle(pairs)
            for i, j in pairs:
                union = rooms[i] | rooms[j]
                xs = [p[0] for p in union]
                ys = [p[1] for p in union]
                if len(union) != (max(xs) - min(xs) + 1) * (max(ys) - min(ys) + 1):
                    rooms[i] = union
                    rooms.pop(j)
                    break
        return rooms

    def render(self, grid=False, floor_color=FLOOR, wall_color=WALL_COLOR, wall_probability=98):
        wall_thickness = WALL
        im = Image.new('RGBA', (self.w * S, self.h * S), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        for x, y in self.cells:
            d.rectangle((x*S, y*S, (x+1)*S-1, (y+1)*S-1), fill=floor_color)
        room_of = {p: i for i, room in enumerate(self.rooms) for p in room}

        # 壁は各格子境界を一度だけ描く。接合部は端を20px延長し、
        # 外壁・内壁とも折れ曲がりの角に隙間が出ないようにする。
        edges = []  # (orientation, grid_x, grid_y, exterior)
        for x, y in self.cells:
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                q = (x+dx, y+dy)
                if q in self.cells:
                    if p_key((x, y)) > p_key(q):
                        continue
                    if frozenset(((x, y), q)) in self.doors:
                        continue
                    if (x, y) in self.corridor and q in self.corridor:
                        continue
                    if (x, y) in room_of and room_of.get(q) == room_of[(x, y)]:
                        continue
                    exterior = False
                else:
                    # 玄関だけは必ず開口にする。その他の外周壁も、下の共通抽選で
                    # 2%の確率で省略され、追加出入口として機能する。
                    if (x, y) == self.entrance and dy == -1:
                        continue
                    exterior = True
                # 内壁・外壁を同じルールで抽選。外周壁が省略されれば追加出入口になる。
                if random.random() < wall_probability / 100.0:
                    if dx:
                        edges.append(('v', x + (dx == 1), y, exterior))
                    else:
                        edges.append(('h', x, y + (dy == 1), exterior))

        # 中心線の上下左右に壁厚の半分ずつ配置。端を延長してT字/L字を密閉。
        # 外壁は外側に飛び出さないよう、最後に床マスクでクリップする。
        wall_layer = Image.new('RGBA', im.size, (0, 0, 0, 0))
        wd = ImageDraw.Draw(wall_layer)
        half = wall_thickness // 2
        for orient, gx, gy, exterior in edges:
            if orient == 'v':
                px, py = gx*S, gy*S
                wd.rectangle((px-half, py-half, px+half-1, py+S+half-1), fill=wall_color)
            else:
                px, py = gx*S, gy*S
                wd.rectangle((px-half, py-half, px+S+half-1, py+half-1), fill=wall_color)

        # 床領域の外にある壁ピクセルは透明化（凹形状の切り欠きも正確）。
        from PIL import ImageChops
        mask = Image.new('L', im.size, 0)
        md = ImageDraw.Draw(mask)
        for x, y in self.cells:
            md.rectangle((x*S, y*S, (x+1)*S-1, (y+1)*S-1), fill=255)
        wall_layer.putalpha(ImageChops.multiply(wall_layer.getchannel('A'), mask))
        im.alpha_composite(wall_layer)

        # 「グリッドあり」の場合、スクウェア境界に幅10pxの黒線を描画する。
        if grid:
            grid_layer = Image.new('RGBA', im.size, (0, 0, 0, 0))
            gd = ImageDraw.Draw(grid_layer)
            grid_width = 10
            half_grid = grid_width // 2
            # 隣接するスクウェア間の境界だけに線を描く。
            for x in range(1, self.w):
                for y in range(self.h):
                    if (x - 1, y) in self.cells and (x, y) in self.cells:
                        gd.rectangle((x*S-half_grid, y*S,
                                      x*S+half_grid-1, (y+1)*S-1),
                                     fill=(0, 0, 0, 255))
            for y in range(1, self.h):
                for x in range(self.w):
                    if (x, y - 1) in self.cells and (x, y) in self.cells:
                        gd.rectangle((x*S, y*S-half_grid,
                                      (x+1)*S-1, y*S+half_grid-1),
                                     fill=(0, 0, 0, 255))
            # 床領域の外側は透明のままにする。
            grid_layer.putalpha(ImageChops.multiply(
                grid_layer.getchannel('A'), mask))
            im.alpha_composite(grid_layer)
        return im


def p_key(p):
    return p[1], p[0]


def hex_to_rgba(value, label):
    """#RRGGBB形式の色指定をRGBAタプルに変換する。"""
    value = value.strip()
    if len(value) != 7 or not value.startswith('#'):
        raise ValueError(f'{label}は #RRGGBB の形式で指定してください。')
    try:
        rgb = tuple(int(value[i:i + 2], 16) for i in (1, 3, 5))
    except ValueError:
        raise ValueError(f'{label}には16進数（0〜9、A〜F）を指定してください。')
    return (*rgb, 255)


class App:
    def __init__(self, root):
        self.root = root
        root.title('建物マップ生成ツール Ver.6')
        top = ttk.Frame(root, padding=12)
        top.pack(fill='x')
        ttk.Label(top, text='横スクウェア数').pack(side='left')
        self.w = tk.IntVar(value=6)
        ttk.Spinbox(top, from_=3, to=99, textvariable=self.w, width=5).pack(side='left', padx=(5,16))
        ttk.Label(top, text='縦スクウェア数').pack(side='left')
        self.h = tk.IntVar(value=8)
        ttk.Spinbox(top, from_=3, to=99, textvariable=self.h, width=5).pack(side='left', padx=(5,16))
        ttk.Button(top, text='新しく生成', command=self.generate).pack(side='left', padx=4)
        ttk.Button(top, text='PNG保存', command=self.save).pack(side='left', padx=4)
        self.rect_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(top, text='長方形にする', variable=self.rect_var,
                        command=self.generate).pack(side='left', padx=8)
        colors = ttk.Frame(root, padding=(12, 0, 12, 0))
        colors.pack(fill='x')
        ttk.Label(colors, text='床の色').pack(side='left')
        self.floor_hex = tk.StringVar(value='#CAA671')
        ttk.Entry(colors, textvariable=self.floor_hex, width=9).pack(side='left', padx=(5, 14))
        ttk.Label(colors, text='壁の色').pack(side='left')
        self.wall_hex = tk.StringVar(value='#414144')
        ttk.Entry(colors, textvariable=self.wall_hex, width=9).pack(side='left', padx=5)
        ttk.Button(colors, text='色を反映', command=self.update_preview).pack(side='left', padx=8)
        ttk.Label(colors, text='壁の生成確率（%）').pack(side='left', padx=(12, 0))
        self.wall_probability = tk.StringVar(value='98')
        ttk.Entry(colors, textvariable=self.wall_probability, width=5).pack(side='left', padx=5)
        self.label = ttk.Label(root)
        self.label.pack(padx=12, pady=12)
        self.grid_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(top, text='グリッドあり', variable=self.grid_var,
                        command=self.update_preview).pack(side='left', padx=8)
        self.info = ttk.Label(root)
        self.info.pack(pady=(0,12))
        self.im = None
        self.generator = None
        self.generate()

    def generate(self):
        try:
            w, h = self.w.get(), self.h.get()
            if not (3 <= w <= 99 and 3 <= h <= 99):
                raise ValueError()
        except (ValueError, tk.TclError):
            messagebox.showerror('入力エラー', '縦横は3〜99の整数にしてください。')
            return
        self.generator = Generator(w, h, rectangular=self.rect_var.get())
        self.update_preview()

    def update_preview(self):
        if self.generator is None:
            return
        w, h = self.generator.w, self.generator.h
        try:
            floor_color = hex_to_rgba(self.floor_hex.get(), '床の色')
            wall_color = hex_to_rgba(self.wall_hex.get(), '壁の色')
            probability = int(self.wall_probability.get().strip())
            if not 0 <= probability <= 100:
                raise ValueError('壁の生成確率は0〜100の整数で指定してください。')
        except ValueError as e:
            messagebox.showerror('入力エラー', str(e) if str(e) else '壁の生成確率は0〜100の整数で指定してください。')
            return
        self.im = self.generator.render(grid=self.grid_var.get(),
                                        floor_color=floor_color,
                                        wall_color=wall_color,
                                        wall_probability=probability)
        preview = self.im.copy()
        preview.thumbnail((850, 650))
        self.photo = ImageTk.PhotoImage(preview)
        self.label.configure(image=self.photo)
        self.info.configure(text=f'画像サイズ：{self.im.width} × {self.im.height} px（1マス{S}px）｜ 部屋数：{len(self.generator.rooms)} ｜ RGBA透過PNG')

    def save(self):
        if self.im is None:
            return
        path = filedialog.asksaveasfilename(defaultextension='.png',
                                            filetypes=[('PNG画像', '*.png')],
                                            initialfile='house_map.png')
        if path:
            self.im.save(path)
            messagebox.showinfo('保存完了', f'保存しました：\n{path}')


if __name__ == '__main__':
    root = tk.Tk()
    App(root)
    root.mainloop()
