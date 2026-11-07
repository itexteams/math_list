import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang18_p4_b2_c2_ds10(self):
        # Khai báo biến
        def round_SA(a): 
            # Kiểm tra nếu a là số nguyên
            if a == int(a):
                return "", int(a)
            
            # Chuyển số thành chuỗi và tách phần nguyên, phần thập phân
            str_a = f"{float(a):.5f}".rstrip('0')  # Giữ tối đa 5 chữ số thập phân, loại bỏ số 0 dư
            integer_part, _, decimal_part = str_a.partition('.')  # Tách phần nguyên và thập phân
            
            # Xác định cách làm tròn
            if len(integer_part) > 2:
                number = Decimal(str(float(a))).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                cirle = "(làm tròn kết quả đến hàng đơn vị)."
            elif len(integer_part) == 2 and len(decimal_part) > 1:
                number = Decimal(str(float(a))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                cirle = "(làm tròn kết quả đến hàng phần chục)."
            elif len(decimal_part) <= 2:
                number = str_a  # Không cần làm tròn thêm
                cirle = ""
            else:
                number = Decimal(str(float(a))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                cirle = "(làm tròn kết quả đến hàng phần trăm)."
            
            # Chuyển dấu chấm thành dấu phẩy (nếu có)
            return cirle, str(number).replace('.', ',')

        # ------------------------------------------------------------------------------BÀI TOÁN
        x, y = sp.symbols('x y')
        
        # Khởi tạo các giá trị ngẫu nhiên
        bien_x, bien_y = random.sample(list(range(25, 40)), 2)
        nuoc = random.choice(["cam", "chanh"])
        an = random.choice(["bắp rang", "khoai chiên"])
        gia_nuoc = random.randint(10, 15)
        gia_an = gia_nuoc + random.randint(2, 5)
        
        # Đảm bảo 2 combo có tỉ lệ thành phần khác nhau để hệ phương trình luôn có nghiệm duy nhất
        danh_sach_combo = [
            (gia_nuoc + gia_an, f"một cốc nước {nuoc} và một túi {an}", 1, 1),
            (round(gia_nuoc + gia_an * 2 * 0.9), f"một cốc nước {nuoc} và hai túi {an}", 1, 2),
            (round(gia_nuoc * 2 * 0.9 + gia_an), f"hai cốc nước {nuoc} và một túi {an}", 2, 1),
            (round(gia_nuoc * 3 * 0.85 + gia_an), f"ba cốc nước {nuoc} và một túi {an}", 3, 1),
            (round(gia_nuoc + gia_an * 3 * 0.85), f"một cốc nước {nuoc} và ba túi {an}", 1, 3),
            (round(gia_nuoc * 3 * 0.8 + gia_an * 2 * 0.85), f"ba cốc nước {nuoc} và hai túi {an}", 3, 2),
            (round(gia_nuoc * 2 * 0.85 + gia_an * 3 * 0.8), f"hai cốc nước {nuoc} và ba túi {an}", 2, 3),
            (round(gia_nuoc * 3 * 0.8 + gia_an * 4 * 0.75), f"ba cốc nước {nuoc} và bốn túi {an}", 3, 4),
            (round(gia_nuoc * 4 * 0.75 + gia_an * 3 * 0.8), f"bốn cốc nước {nuoc} và ba túi {an}", 4, 3)
        ]

        while True:
            compo1, compo2 = random.sample(danh_sach_combo, 2)
            gia1, thuc_don1, so_nuoc1, so_an1 = compo1
            gia2, thuc_don2, so_nuoc2, so_an2 = compo2
            # Định thức khác 0 để hệ phương trình luôn xác định nghiệm duy nhất B
            if so_nuoc1 * so_an2 - so_nuoc2 * so_an1 != 0:
                break

        max_nuoc = so_nuoc1 * bien_x + so_nuoc2 * bien_y
        max_an = so_an1 * bien_x + so_an2 * bien_y

        Eq1 = so_nuoc1 * x + so_nuoc2 * y
        Eq2 = so_an1 * x + so_an2 * y

        # SỬA LỖI: dùng sp.solve thay vì solve tự do để tránh conflict namespace
        nghiem = sp.solve([sp.Eq(Eq1, max_nuoc), sp.Eq(Eq2, max_an)], (x, y))
        ham_F = gia1 * x + gia2 * y
        
        xA, yA = min([sp.Rational(max_nuoc, so_nuoc1), sp.Rational(max_an, so_an1)]), 0
        yC, xC = min([sp.Rational(max_nuoc, so_nuoc2), sp.Rational(max_an, so_an2)]), 0
        xB, yB = nghiem[x], nghiem[y]

        toa_do_cac_dinh = [(0, 0), (xA, yA), (xB, yB), (xC, yC)]
        cac_gia_tri = [ham_F.subs({x: dinh[0], y: dinh[1]}) for dinh in toa_do_cac_dinh]
        so_dinh = len(toa_do_cac_dinh)
        ket_qua = max(cac_gia_tri)
        max_index = cac_gia_tri.index(ket_qua)
        max_dinh = toa_do_cac_dinh[max_index]

        xmin = -1 if min(xA, xB) < 11 else -3 if min(xA, xB) < 21 else -4 
        xmax = (1 if max(xA, xB) < 11 else 3 if max(xA, xB) < 21 else 4) + round(float(max(xA, xB)), 1)
        ymin = -1 if min(yC, yB) < 11 else -3 if min(yC, yB) < 21 else -4  
        ymax = (1 if max(yC, yB) < 11 else 3 if max(yC, yB) < 21 else 4) + round(float(max(yC, yB)), 1)
        
        scale_val = 0.7 if abs(ymax-ymin) < 6 else 0.5 if abs(ymax-ymin) < 11 else 0.25 if abs(ymax-ymin) < 21 else 0.1 if abs(ymax-ymin) < 31 else 0.08

        # Vẽ hình bằng TikZ theo phong cách gạch sọc
        tikz_latex = f'''\\begin{{tikzpicture}}[>=stealth, scale={scale_val}, line width=1pt, font=\\footnotesize]
    \\clip ({xmin},{ymin}) rectangle ({xmax},{ymax});
    \\fill[pattern=north east lines, pattern color=black] ({xmin},{ymin}) rectangle ({xmax},{ymax});
    %% Vì xC=0 và yA=0 nên tọa độ là O(0,0), A(xA,0), B(xB,yB), C(0,yC)
    \\fill[white] (0,0) -- ({xA},0) -- ({xB},{yB}) -- (0,{yC}) -- cycle;
    \\coordinate (O) at (0,0);
    \\coordinate (A) at ({xA},0);
    \\coordinate (B) at ({xB},{yB});
    \\coordinate (C) at (0,{yC});
    \\draw[black] ($(A)!-30cm!(B)$) -- ($(B)!-30cm!(A)$);
    \\draw[black] ($(C)!-30cm!(B)$) -- ($(B)!-30cm!(C)$);
    \\draw[->] ({xmin},0) -- ({xmax},0) node[below] {{$x$}};
    \\draw[->] (0,{ymin}) -- (0,{ymax}) node[left] {{$y$}};
    \\node at (0,0) [below left] {{$O$}};
    \\node at ({xA},0) [above right] {{${sp.latex(xA)}$}};
    \\node at (0,{yC}) [above right] {{${sp.latex(yC)}$}};
    \\fill (A) circle (1.5pt) node[below left] {{$A$}};
    \\fill (B) circle (1.5pt) node[above right] {{$B$}};
    \\fill (C) circle (1.5pt) node[below left] {{$C$}};
    \\draw[dashed] ({xB},0) node[below] {{${sp.latex(xB)}$}} |- (0,{yB}) node[left] {{${sp.latex(yB)}$}};
\\end{{tikzpicture}}'''

        noidungcauhoi = f"""Để gây quỹ từ thiện, câu lạc bộ thiện nguyện của một trường THPT tổ chức hoạt động bán hàng với hai mặt hàng là nước {nuoc} và {an}. 
                            Câu lạc bộ thiết kế hai thực đơn. 
                            Thực đơn 1 có giá ${gia1}$ nghìn đồng, bao gồm {thuc_don1}.
                            Thực đơn 2 có giá ${gia2}$ nghìn đồng, bao gồm {thuc_don2}.
                            Biết rằng câu lạc bộ chỉ làm được không quá ${max_nuoc}$ cốc nước {nuoc} và ${max_an}$ túi {an}. 
                            Tính số tiền lớn nhất mà câu lạc bộ có thể nhận được sau khi bán hết hàng {round_SA(ket_qua)[0]}."""
        
        loigiai = f""" \\immini{{
                            Gọi $x$ và $y$ theo thứ tự là số thực đơn 1 và thực đơn 2 được bán ra.\\\\
                            Theo đề bài ta có hệ bất phương trình 
                            $$\\begin{{cases}}
                                x \\ge 0 \\\\
                                y \\ge 0 \\\\
                                {sp.latex(Eq1)} \\le {sp.latex(max_nuoc)} \\\\
                                {sp.latex(Eq2)} \\le {sp.latex(max_an)} 
                            \\end{{cases}}$$
                            Số tiền câu lạc bộ thu được là $F(x; y) = {sp.latex(ham_F)}$.\\\\
                            Miền nghiệm của hệ bất phương trình trên là miền tứ giác $OABC$ với tọa độ các đỉnh $O$, $A$, $B$, $C$ theo thứ tự trong bảng dưới đây:
                            \\begin{{center}} 
                                \\begin{{tabular}}{{{'|c' * (so_dinh + 1)}|}}  \n  \\hline
                                    {"&".join(['$(x; y)$'] + [f"$\\left({sp.latex(dinh[0])}; {sp.latex(dinh[1])}\\right)$" for dinh in toa_do_cac_dinh]) + "\\\\ \n\\hline"}
                                    {"&".join(['$F(x; y)$'] + [f"${round_SA(gia_tri)[1]}$" for gia_tri in cac_gia_tri]) + "\\\\ \n\\hline"}
                                \\end{{tabular}}
                            \\end{{center}}
                            Số tiền lớn nhất mà câu lạc bộ có thể nhận được sau khi bán hết hàng là ${round_SA(ket_qua)[1]}$ nghìn đồng, 
                            tương ứng với bán được ${sp.latex(max_dinh[0])}$ thực đơn 1 và ${sp.latex(max_dinh[1])}$ thực đơn 2.
                        }}{{{tikz_latex}}} """

        # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
        content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + str(noidungcauhoi) +
                    '\n\\loigiai{ \n'
                    + str(loigiai) + '\n}\n'
                    '\\end{ex}\n \\end{minipage} \n\n').replace('$zz$', '.').replace('\\frac', '\\dfrac')
        return content