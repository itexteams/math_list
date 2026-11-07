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


def bt_dang7_p3_b1_c2_ds10(self):
                # Khai báo biến
                lisdang = ['1']
                dang = random.choice(lisdang)
                
                if dang == '1':
                    # B3: Tạo tập hợp các cặp tọa độ (x0, y0) nguyên đẹp trong khoảng [-4, 4]
                    # sao cho hệ số góc p = -y0/x0 là một số nguyên
                    valid_pairs = []
                    for x_val in [-4, -3, -2, -1, 1, 2, 3, 4]:
                        for y_val in [-4, -3, -2, -1, 1, 2, 3, 4]:
                            if y_val % x_val == 0:
                                valid_pairs.append((x_val, y_val))
                                
                    x0, y0 = random.choice(valid_pairs)
                    p = -y0 // x0  # Hệ số góc nguyên
                    
                    # Random xem gốc O(0,0) thuộc miền tô đậm hay không tô đậm
                    o_in_solution = random.choice([True, False])
                    
                    # Xác định hệ số a, b, c dựa vào việc O có thuộc miền nghiệm hay không
                    if o_in_solution:
                        mien_chu_O = "không bị gạch chéo (miền trắng)"
                        if y0 > 0:
                            a, b, c = p, -1, y0
                        else:
                            a, b, c = -p, 1, -y0
                    else:
                        mien_chu_O = "bị gạch chéo"
                        if y0 < 0:
                            a, b, c = p, -1, y0
                        else:
                            a, b, c = -p, 1, -y0
                
                    # Tính tổng S
                    S_val = a + b + c
                
                    # Tạo chuỗi hiển thị phương trình đường thẳng y = px + q chuẩn dấu
                    str_p = "" if p == 1 else "-" if p == -1 else str(p)
                    str_q = f" + {y0}" if y0 > 0 else f" - {abs(y0)}"
                    line_y_eq = f"y = {str_p}x{str_q}"
                
                    # Tạo chuỗi hiển thị biểu thức ax + by + c chuẩn dấu
                    str_a = "x" if a == 1 else "-x" if a == -1 else f"{a}x"
                    str_b = " + y" if b == 1 else " - y" if b == -1 else (f" + {b}y" if b > 0 else f" - {abs(b)}y")
                    str_c = f" + {c}" if c > 0 else f" - {abs(c)}"
                    
                    bieu_thuc_abc = f"{str_a}{str_b}{str_c}"
                    line_abc_eq = f"{bieu_thuc_abc} = 0"
                    bpt_abc = f"{bieu_thuc_abc} > 0"
                
                    # Định dạng chuỗi thế số vào tính toán chuẩn dấu
                    sign_b = "+" if b >= 0 else "-"
                    sign_c = "+" if c >= 0 else "-"
                    dau_so_sanh = ">" if c > 0 else "<"
                    the_so_str = f"{a}\\cdot 0 {sign_b} {abs(b)}\\cdot 0 {sign_c} {abs(c)} = {c} {dau_so_sanh} 0"
                
                    # Định dạng chuỗi tính tổng S chuẩn dấu
                    str_b_S = f" + {b}" if b >= 0 else f" - {abs(b)}"
                    str_c_S = f" + {c}" if c >= 0 else f" - {abs(c)}"
                    tinh_S_str = f"{a}{str_b_S}{str_c_S} = {S_val}"
                
                    # ==========================================
                    # Xây dựng code TikZ theo phong cách mới
                    # ==========================================
                    y_at_min10 = p * (-10) + y0
                    y_at_max10 = p * 10 + y0
                    
                    # Xác định miền trắng (miền nghiệm)
                    if b == -1:
                        # y < px + y0 -> miền trắng nằm dưới đường thẳng
                        white_fill = f"\\fill[white] (-10, {y_at_min10}) -- (10, {y_at_max10}) -- (10, -20) -- (-10, -20) -- cycle;"
                    else:
                        # y > px + y0 -> miền trắng nằm trên đường thẳng
                        white_fill = f"\\fill[white] (-10, {y_at_min10}) -- (10, {y_at_max10}) -- (10, 20) -- (-10, 20) -- cycle;"
                
                    # Tìm vị trí đặt nhãn đường thẳng d
                    if p > 0:
                        y_test = p * 4 + y0
                        if -5 <= y_test <= 5:
                            x_d, y_d = 4, y_test
                            pos_d = "above left"
                        else:
                            y_d = 4.5
                            x_d = (4.5 - y0) / p
                            pos_d = "above left"
                    else:
                        y_test = p * (-4) + y0
                        if -5 <= y_test <= 5:
                            x_d, y_d = -4, y_test
                            pos_d = "above right"
                        else:
                            y_d = 4.5
                            x_d = (4.5 - y0) / p
                            pos_d = "above right"
                
                    tikz_code = f"""\\begin{{center}}
\\begin{{tikzpicture}}[>=stealth, scale=0.8, line width=1pt]
\\clip (-5,-5) rectangle (5,5);
\\fill[pattern=north east lines, pattern color=black] (-5,-5) rectangle (5,5);
{white_fill}
\\draw[black] (-10, {y_at_min10}) -- (10, {y_at_max10});
\\foreach \\x in {{-4,-3,-2,-1,1,2,3,4}}
  \\draw (\\x,0.1) -- (\\x,-0.1) node[below, fill=white, inner sep=1pt, font=\\footnotesize] {{$\\x$}};
\\foreach \\y in {{-4,-3,-2,-1,1,2,3,4}}
  \\draw (0.1,\\y) -- (-0.1,\\y) node[left, fill=white, inner sep=1pt, font=\\footnotesize] {{$\\y$}};
\\coordinate (A) at ({x0}, 0);
\\coordinate (B) at (0, {y0});
\\fill (A) circle (0.5pt);
\\fill (B) circle (0.5pt);
\\node[{pos_d}] at ({round(x_d, 2)}, {round(y_d, 2)}) {{$d$}};
\\draw[->] (-5, 0) -- (5, 0) node[below] {{$x$}};
\\draw[->] (0, -5) -- (0, 5) node[left] {{$y$}};
\\node at (0,0) [below left] {{$O$}};
\\end{{tikzpicture}}
\\end{{center}}"""
                
                    # Các đáp án trắc nghiệm
                    du = ['$%s$' % (S_val)]
                    da = random.choice(du)
                    
                    # Tạo các đáp án sai không trùng lắp
                    s = [
                        '$%s$' % (S_val + 1),
                        '$%s$' % (S_val - 1),
                        '$%s$' % (S_val + 2),
                        '$%s$' % (S_val - 2),
                        '$%s$' % (S_val + 4),
                        '$%s$' % (-S_val),
                    ]
                    s = list(set(s))
                    if da in s: s.remove(da)
                
                    das1, das2, das3 = random.sample(s, 3)
                
                    # Đề bài
                    noidungcauhoi = ('''Miền trắng (không kể bờ $d$) trong hình dưới đây là miền nghiệm của bất phương trình $ax + by %s > 0$. Tính $S = a + b + c$\n''' % (str_c) + tikz_code)
                
                    # Các đáp án
                    da_d = ('\\True ' + str(da))
                    da_s1 = str(das1)
                    da_s2 = str(das2) 
                    da_s3 = str(das3) 
                    
                    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                    list_1 = [da_d, da_s1, da_s2, da_s3]
                    random.shuffle(list_1)
                    
                    # Nội dung lời giải
                    loigiai = ('''Gọi bờ $(d)$ là đường thẳng có dạng $y = px + q$ \\\\
Ta có: $(d)$ đi qua điểm $(%s;0)$ và $(0;%s)$ được đánh dấu trên trục tọa độ nên ta có hệ phương trình: $\\begin{cases} 0 = %sp + q \\\\ %s = 0p + q \\end{cases} \\Leftrightarrow \\begin{cases} p = %s \\\\ q = %s \\end{cases}$ \\\\
$\\Rightarrow (d) : %s$ hay $(d) : %s$. \\\\
Chọn $O(0;0)$ là điểm thuộc miền %s. Thay $O(0;0)$ vào biểu thức $ax+by+c$, ta được: \\\\
$%s$ \\\\
Vậy miền trắng (không gạch chéo) trong hình là miền nghiệm của bất phương trình $%s$. \\\\
Đồng nhất hệ số với bất phương trình đề bài $ax + by %s > 0$, ta suy ra: $a = %s, b = %s, c = %s$. \\\\
Vậy $S = %s$'''
                                   % (x0, y0, x0, y0, p, y0,
                                      line_y_eq, line_abc_eq,
                                      mien_chu_O,
                                      the_so_str,
                                      bpt_abc,
                                      str_c, a, b, c,
                                      tinh_S_str))
                    dapan = '\\shortans[0]{$%s$}\n' % (tinh_S_str)
                
                    # Xuất câu trắc nghiệm
                    content = ('\\begin{minipage}{\\textwidth} \n'
                        '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                        '\\loigiai{\n'+str(loigiai)+'\n}\n'
                        '\\end{ex}\n \\end{minipage} \n\n')
                    return content