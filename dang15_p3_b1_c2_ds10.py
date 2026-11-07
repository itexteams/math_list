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


def bt_dang15_p3_b1_c2_ds10(self):
                # Khai báo biến
                lisdang = ['1']
                dang = random.choice(lisdang)
                
                if dang == '1':
                    # Random các hệ số a, b, c nguyên dương
                    a = random.randint(2, 7)
                    b = random.randint(1, 7)
                    c = random.randint(2, 7)
                    
                    # Hàm xử lý hệ số 1 và dấu (Tránh tình trạng 1x, 1y hay + -)
                    def format_eq(coef_a, coef_b):
                        term_x = "x" if coef_a == 1 else f"{coef_a}x"
                        term_y = "y" if coef_b == 1 else f"{coef_b}y"
                        return f"{term_x} + {term_y}" # Vì a,b > 0 nên luôn là dấu +
                        
                    eq_str = format_eq(a, b)
                    
                    # Giao điểm với các trục tọa độ
                    x_int = Rational(c, a)
                    y_int = Rational(c, b)
                    
                    # Tính diện tích tam giác
                    S_val = (c**2) / (2 * a * b)
                    
                    # ==========================================
                    # BƯỚC LÀM TRÒN KẾT QUẢ ĐẾN HÀNG PHẦN CHỤC
                    # ==========================================
                    S_rounded = Decimal(float(S_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    kq_str = str(S_rounded).replace('.', ',')
                
                    # Các đáp án trắc nghiệm
                    du = [f'${kq_str}$']
                    da = random.choice(du)
                
                    # Đề bài
                    noidungcauhoi = f"Miền nghiệm của bất phương trình ${eq_str} \\le {c}$ giới hạn bởi $2$ tia $Ox, Oy$ có diện tích bằng bao nhiêu (làm tròn kết quả đến hàng phần chục)?"
                
                    # Mã TikZ động dựa trên các thông số đã random
                    xmax = float(c/a) + 1.5
                    ymax = float(c/b) + 1.5
                    
                    # Phần vẽ TikZ đã được thay đổi \fill
                    tikz = f'''\\begin{{center}}
    \\begin{{tikzpicture}}[>=stealth, scale=1]
    \\clip (-1.3, -1.3) rectangle ({xmax+0.5}, {ymax+0.5});
    \\fill[pattern=north east lines, pattern color=black] (-2, {float((c - a*(-2))/b)}) -- ({xmax+2}, {float((c - a*(xmax+2))/b)}) -- ({xmax+2}, {ymax+2}) -- (-2, {ymax+2}) -- cycle;
    \\draw[thick] (-2, {float((c - a*(-2))/b)}) -- ({xmax+1}, {float((c - a*(xmax+1))/b)}) node[pos=0.25, left] {{$\\Delta$}};
    \\fill (0,{float(c/b)}) circle (0.5pt) node[left] {{${latex(y_int)}$}};
    \\fill ({float(c/a)},0) circle (0.5pt) node[below left] {{${latex(x_int)}$}};
    \\draw[->] (-1,0) -- ({xmax},0) node[above] {{$x$}};
    \\draw[->] (0,-1) -- (0,{ymax}) node[right] {{$y$}};
    \\node at (0,0) [below left] {{$O$}};
    \\end{{tikzpicture}}
    \\end{{center}}'''
                    
                    # Lời giải chi tiết
                    loigiai = (f'''Vẽ đường thẳng $\\Delta: {eq_str} = {c}$.\\\\ \n'''
                               f'''Lấy gốc tọa độ $O(0;0)$, ta thấy $O \\notin \\Delta$ và có ${a} \\cdot 0 + {b} \\cdot 0 < {c}$ nên nửa mặt phẳng bờ $\\Delta$ chứa gốc tọa độ $O$ là miền nghiệm của bất phương trình đã cho.\\\\ \n'''
                               f'''{tikz} \n'''
                               f'''Miền nghiệm của bất phương trình ${eq_str} \\le {c}$ giới hạn bởi 2 tia $Ox, Oy$ là một tam giác có diện tích bằng $\\frac{{1}}{{2}} \\cdot {latex(x_int)} \\cdot {latex(y_int)} = {latex(Rational(c**2, 2*a*b))} \\approx {kq_str}$.''')
                
                    # Đáp án
                    dapan = '\\shortans[0]{$%s$}\n' % (latex(kq_str))
                
                    # Xuất câu hỏi với đáp án và lời giải
                    content = ('\\begin{minipage}{\\textwidth} \n'
                        '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
                        '\\loigiai{ \n'
                        + str(loigiai) + '}\n'
                        '\\end{ex}\n \\end{minipage} \n\n')
                    return content