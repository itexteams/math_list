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


def bt_dang32_p3_b2_c1_ds12(self):
        # Khai báo hàm làm tròn
        def round_SA(a): 
            val = float(a)
            if val.is_integer():
                return "", str(int(val))
            
            str_a = f"{val:.5f}".rstrip('0')
            integer_part, _, decimal_part = str_a.partition('.')
            
            if len(integer_part) > 2:
                number = Decimal(str(val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                cirle = "(làm tròn kết quả đến hàng đơn vị)."
            elif len(integer_part) == 2 and len(decimal_part) > 1:
                number = Decimal(str(val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                cirle = "(làm tròn kết quả đến hàng phần chục)."
            elif len(decimal_part) <= 2:
                number = Decimal(str_a)
                cirle = ""
            else:
                number = Decimal(str(val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                cirle = "(làm tròn kết quả đến hàng phần trăm)."
            
            return cirle, str(number).replace('.', ',')

        # ------------------------------------------------------------------------------BÀI TOÁN
        # 1. Sinh ngẫu nhiên các giá trị gốc cho bài toán
        W = random.randint(2, 5)                # Chiều rộng sông (km)
        L = random.randint(W + 3, 12)           # Khoảng cách hạ lưu (km)
        v_cheo = random.randint(3, 6)           # Tốc độ chèo (km/h)
        v_chay = random.randint(v_cheo + 1, 10) # Tốc độ chạy (km/h)

        x = symbols('x', positive=True, real=True)

        # 2. Giải bài toán
        # Hàm tổng thời gian T(x)
        ham_T = sp.sqrt(W**2 + x**2) / v_cheo + (L - x) / v_chay
        T_prime = sp.diff(ham_T, x)

        try:
            solutions = sp.solve(sp.Eq(T_prime, 0), x)
            pos_sols = [sol for sol in solutions if sol.is_real and sol > 0]
            x_candidate = pos_sols[0] if pos_sols else (W * v_cheo) / sp.sqrt(v_chay**2 - v_cheo**2)
        except Exception:
            x_candidate = (W * v_cheo) / sp.sqrt(v_chay**2 - v_cheo**2)

        if float(x_candidate) >= L:
            x_final = L
        else:
            x_final = x_candidate

        # Tính kết quả thời gian nhỏ nhất
        ket_qua = ham_T.subs(x, x_final)

        # 3. Mã TikZ để vẽ hình minh họa
        scale_val = 0.4 if L > 7 else 0.6
        d_coord = min(4, L - 1)
        tikz_code = f"""\\begin{{tikzpicture}}[scale={scale_val},line width=1pt,line cap=round,line join=round,font=\\footnotesize]
\\def\\width{{{W}}}
\\def\\height{{{L}}}
\\fill[cyan!30] (0,0) rectangle (\\width,\\height);
\\draw[thick] (0,0) rectangle (0,\\height)
             (\\width,0) rectangle (\\width,\\height);
\\foreach \\x in {{0.5,1.5,2.5}} {{
    \\draw[white, line width=1pt, decorate, decoration={{snake, segment length=10pt, amplitude=2pt}}] 
    (\\x,0) -- (\\x,\\height);
}}
\\coordinate (A) at (0,\\height);
\\coordinate (B) at (\\width,0);
\\coordinate (C) at (\\width,\\height);
\\coordinate (D) at (\\width,{d_coord});
\\draw[->, thick, blue] (A) -- (C);
\\draw[->, thick, magenta] (A) -- (D);
\\draw[->, thick, green!70!black] (A) -- (B);
\\node[left] at (A) {{$A$}};
\\node[right] at (B) {{$B$}};
\\node[right] at (C) {{$C$}};
\\node[right] at (D) {{$D$}};
\\draw[<->, thick] (0,\\height+0.8) -- (\\width,\\height+0.8);
\\node at (\\width/2,\\height+1.5) {{${W}$ km}};
\\draw[<->, thick] (\\width+1.5,0) -- (\\width+1.5,\\height);
\\node at (\\width+3,\\height/2) {{${L}$ km}};
\\end{{tikzpicture}}"""

        cirle_text, kq_str = round_SA(ket_qua)

        noidungcauhoi = f"""\\immini{{Một người chèo thuyền từ điểm $A$ trên bờ một con sông thẳng, rộng ${W}$ km. Người đó muốn đến điểm $B$ ở bờ đối diện, cách bờ đối diện ${L}$ km về phía hạ lưu trong thời gian nhanh nhất.
Biết rằng tốc độ chèo thuyền của người này là ${v_cheo}$ km/h và tốc độ chạy bộ dọc bờ sông là ${v_chay}$ km/h. Giả sử vận tốc dòng nước không đáng kể.
Thời gian ngắn nhất người này có thể đi từ $A$ đến $B$ là bao nhiêu giờ? {cirle_text}
}}{{{tikz_code}}}"""

        x_val_flt = float(x_final)
        x_str_approx = f" \\approx {round_SA(x_val_flt)[1]}" if not x_val_flt.is_integer() else ""

        loigiai = f"""Gọi $W$ là chiều rộng con sông, $L$ là khoảng cách hạ lưu đến $B$.\\\\
Ta có $W = {W}\\text{{ km}}$, $L = {L}\\text{{ km}}$.\\\\
Gọi $v_1$ là tốc độ chèo thuyền, $v_2$ là tốc độ chạy bộ. Ta có $v_1 = {v_cheo}\\text{{ km/h}}$, $v_2 = {v_chay}\\text{{ km/h}}$.\\\\
Gọi $D$ là điểm người đó cập bờ, đặt $x$ là khoảng cách $CD$ (với $0 \\le x \\le {L}$).\\\\
Quãng đường chèo thuyền là $AD$. Áp dụng định lý Pytago, ta có:
$$AD = \\sqrt{{W^2 + x^2}} = \\sqrt{{{W**2} + x^2}}.$$
Thời gian chèo thuyền là:
$$t_1 = \\dfrac{{AD}}{{v_1}} = \\dfrac{{\\sqrt{{{W**2} + x^2}}}}{{{v_cheo}}}.$$
Quãng đường chạy bộ là $DB = CB - CD = {L} - x$.\\\\
Thời gian chạy bộ là:
$$t_2 = \\dfrac{{DB}}{{v_2}} = \\dfrac{{{L} - x}}{{{v_chay}}}.$$
Tổng thời gian di chuyển là một hàm theo biến $x$:
$$T(x) = t_1 + t_2 = \\dfrac{{\\sqrt{{{W**2} + x^2}}}}{{{v_cheo}}} + \\dfrac{{{L} - x}}{{{v_chay}}}.$$
Ta cần tìm giá trị nhỏ nhất của hàm $T(x)$ trên đoạn $[0; {L}]$.\\\\
Đạo hàm của $T(x)$:
$$T'(x) = {sp.latex(T_prime)}.$$
Giải phương trình $T'(x) = 0 \\Leftrightarrow \\dfrac{{x}}{{{v_cheo}\\sqrt{{{W**2} + x^2}}}} = \\dfrac{{1}}{{{v_chay}}}$
$$\\Leftrightarrow x = {sp.latex(x_final)}{x_str_approx}.$$
Vì $x \\in [0; {L}]$ nên hàm số đạt giá trị nhỏ nhất tại điểm này.\\\\
Thay giá trị $x$ vào hàm $T(x)$, ta được thời gian ngắn nhất là:
$$T_{{\\min}} = {sp.latex(ket_qua)} \\approx {kq_str}\\text{{ giờ.}}$$"""

        # Đáp án ngắn
        dapan = f'\\shortans[0]{{${kq_str}$}}'

        content = ('\\begin{minipage}{\\textwidth}\n'
                   '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) + '\n'
                   '\\loigiai{\n' + str(loigiai) + '}\n'
                   '\\end{ex}\n\\end{minipage}\n\n').replace('$zz$', '.').replace('\\frac', '\\dfrac')

        return content