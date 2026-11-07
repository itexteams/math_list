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


def bt_dang15_p2_b1_c3_hh10(self):
                # 1. KHAI BÁO BIẾN NGẪU NHIÊN
                x = symbols('x')
                list_b = [Rational(3, 2), Rational(1, 1), Rational(2, 1), Rational(5, 2)]
                list_a = [Rational(1, 2), Rational(2, 5), Rational(3, 5), Rational(4, 5)]
                
                b_val = random.choice(list_b)
                a_val = random.choice(list_a)
                
                # Chọn điểm hiển thị trên đồ thị
                x1 = 7 
                y1 = a_val * x1 + b_val
                ham_so = a_val * x + b_val
                
                # 2. NỘI DUNG CÂU HỎI (TIK Z)
                noidungcauhoi = (r'''Để tham gia một phòng tập thể dục, người tập phải trả một khoản phí tham gia ban đầu và phí sử dụng phòng tập. Đường thẳng $\Delta$ ở hình dưới biểu thị tổng chi phí (đơn vị: triệu đồng) tham gia một phòng tập thể dục theo thời gian tập của một người (đơn vị: tháng).
    \begin{center}
    \begin{tikzpicture}[>=stealth, x=0.5cm, y=0.5cm, scale=0.8]
        \draw[->] (-1,0) -- (15,0) node[below] {$x$};
        \draw[->] (0,-1) -- (0,10) node[left] {$y$};
        \node[below left] at (0,0) {$O$};
        \node[below] at (7.5,-1) {Tháng};
        \node[rotate=90, above] at (-2.5,5) {Chi phí (triệu đồng)};
        \draw[domain=0:13, thick, variable=\x] plot (\x, {%s*\x + %s});
        \node[left]  at (12.5, {%s*12 + %s + 0.5}) {$\Delta$};
        \draw[dashed] (%s,0) -- (%s,%s) -- (0,%s);
        \node[below] at (%s,0) {$%s$};
        \node[left] at (0,%s) {$%s$};
        \node[left] at (0,%s) {$%s$};
        \fill (0,%s) circle (1.5pt);
        \fill (%s,%s) circle (1.5pt);
    \end{tikzpicture}
    \end{center}
    Xét tính đúng sai của các mệnh đề sau:''' 
                % (float(a_val), float(b_val), float(a_val), float(b_val), 
                x1, x1, float(y1), float(y1), 
                x1, x1, 
                float(y1), latex(y1), 
                float(b_val), latex(b_val),
                float(b_val), x1, float(y1)))

                # 3. CHUẨN BỊ CÁC CẶP ĐÁP ÁN (ĐÚNG - SAI) CHO MỖI Ý
                
                # Ý a: Phương trình đường thẳng
                pt_sai = (a_val + Rational(1,2)) * x + b_val
                list_da_a = [
                    '\\True Phương trình của đường thẳng $\\Delta$ là $y = %s$' % (latex(ham_so)),
                    'Phương trình của đường thẳng $\\Delta$ là $y = %s$' % (latex(pt_sai))
                ]
                loigiai_a = ('''Gọi phương trình đường thẳng $\\Delta$ là $y = ax + b$. \\\\ Đường thẳng đi qua điểm $(0; %s)$ nên $b = %s$. \\\\ Đường thẳng đi qua điểm $\\left(%s; %s\\right)$ nên: $%s = a \\cdot %s + %s \\Leftrightarrow a = %s$. \\\\ Vậy phương trình là $y = %s$.''' 
                            % (latex(b_val), latex(b_val), x1, latex(y1), latex(y1), x1, latex(b_val), latex(a_val), latex(ham_so)))

                # Ý b: Ý nghĩa giao điểm trục tung
                list_da_b = [
                    '\\True Giao điểm của đường thẳng $\\Delta$ với trục tung là khoản phí tham gia ban đầu: $%s$ triệu đồng' % (latex(b_val)),
                    'Giao điểm của đường thẳng $\\Delta$ với trục tung là khoản phí sử dụng hàng tháng: $%s$ triệu đồng' % (latex(b_val))
                ]
                loigiai_b = ('''Tại $x=0$, chi phí tương ứng là giao điểm với trục tung. Đây là khoản phí cố định ban đầu. Từ hình vẽ, giá trị này là $%s$ triệu đồng.''' % (latex(b_val)))

                # Ý c: Tỉ lệ chi phí
                y6 = a_val * 6 + b_val
                y3 = a_val * 3 + b_val
                tile = y6 / y3
                list_da_c = [
                    '\\True Tổng chi phí 6 tháng không gấp đôi tổng chi phí 3 tháng',
                    'Tổng chi phí 6 tháng gấp đôi tổng chi phí 3 tháng'
                ]
                loigiai_c = ('''$y(3) = %s$; $y(6) = %s$. Tỉ số $\\frac{y(6)}{y(3)} = \\frac{%s}{%s} \\approx %s \\neq 2$.''' 
                            % (latex(y3), latex(y6), latex(y6), latex(y3), round(float(tile),2)))

                # Ý d: Tính toán cụ thể 12 tháng
                y12_dung = a_val * 12 + b_val
                y12_sai = y12_dung + 1
                list_da_d = [
                    '\\True Tổng chi phí sau 12 tháng là $%s$ triệu đồng' % (latex(y12_dung)),
                    'Tổng chi phí sau 12 tháng là $%s$ triệu đồng' % (latex(y12_sai))
                ]
                loigiai_d = ('''Với $x=12$, ta có $y = %s \\cdot 12 + %s = %s$ triệu đồng.''' % (latex(a_val), latex(b_val), latex(y12_dung)))

                # 4. VÒNG LẶP CHỌN ĐÁP ÁN (Đảm bảo 1-3 câu đúng)
                def count_true(ans_list):
                    return sum('\\True' in s for s in ans_list)

                while True:
                    d1 = random.choice(list_da_a)
                    d2 = random.choice(list_da_b)
                    d3 = random.choice(list_da_c)
                    d4 = random.choice(list_da_d)
                    
                    if 1 <= count_true([d1, d2, d3, d4]) <= 3:
                        final_answers = [d1, d2, d3, d4]
                        final_solutions = [loigiai_a, loigiai_b, loigiai_c, loigiai_d]
                        break

                # 5. XUẤT NỘI DUNG RA FILE/CONSOLES
                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + 
                    str(noidungcauhoi) + '\n'
                    '\\choiceTFn \n'
                    '{' + str(final_answers[0]) + '}\n'
                    '{' + str(final_answers[1]) + '}\n'
                    '{' + str(final_answers[2]) + '}\n'
                    '{' + str(final_answers[3]) + '}\n'
                    '\\loigiai{ \n'
                    '\\begin{enumEX}[a)]{1} \n'
                    '\\item ' + str(final_solutions[0]) + '\n'
                    '\\item ' + str(final_solutions[1]) + '\n'
                    '\\item ' + str(final_solutions[2]) + '\n'
                    '\\item ' + str(final_solutions[3]) + '\n'
                    '\\end{enumEX}} \n'
                    '\\end{ex}\n \\end{minipage} \n\n')
                return content   