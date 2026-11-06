import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

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


def bt_dang73_p1_b1_c4_ds10(self):
            #Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các thông số đầu bài
                a = random.choice([6, 8, 10])     # Cạnh hình vuông ABCD
                k1 = random.choice([2, 3])        # Đoạn AE
                k2 = random.choice([3, 4])        # Đoạn BF

                # Tính toán giá trị tối ưu theo logic bài toán
                # Điều kiện đồng dạng: AE/CG = AH/CF => k1/y = x/(a - k2) => xy = k1*(a - k2)
                const_xy = k1 * (a - k2)

                # Biểu thức cần tối ưu (từ lời giải): (a-k1)x + (a-k2)y
                # Theo AM-GM: (a-k1)x = (a-k2)y => (a-k1)x = (a-k2)*(const_xy/x)
                coeff_x = a - k1
                coeff_y_numerator = (a - k2) * const_xy

                # Tìm x, y và tổng x+y
                x_val_sq = Rational(coeff_y_numerator, coeff_x)
                x_val = simplify(sqrt(x_val_sq))
                y_val = simplify(const_xy / x_val)
                tong_xy = simplify(x_val + y_val)

                # Kết quả đúng
                kq = '$%s$' % latex(tong_xy)

                # ==========================================
                # BƯỚC 4: TẠO CÁC PHƯƠNG ÁN SAI
                # ==========================================
                s = []
                # Các độ lệch để tạo đáp án nhiễu
                offsets = [Rational(1, 2), Rational(3, 2), 1, 2, sqrt(2), sqrt(3)]
                while len(s) < 3:
                    offset = random.choice(offsets)
                    variant = simplify(tong_xy + (random.choice([-1, 1]) * offset))
                    variant_latex = '$%s$' % latex(variant)
                    # Đảm bảo không trùng đáp án đúng và các đáp án sai khác
                    if variant_latex != kq and variant_latex not in s:
                        s.append(variant_latex)

                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # ==========================================
                # VẼ HÌNH TIKZ ĐỘNG
                # ==========================================
                # Tỷ lệ vẽ (scale) để hình không quá to
                sc = 0.6
                # Điểm G và H trên hình vẽ minh họa (tương đối để nhìn đẹp)
                x_draw = a * 0.6
                y_draw = a * 0.4

                # Lưu ý: Sử dụng chuỗi f-string hoặc cộng chuỗi để tránh lỗi % với TikZ
                tikz_code = r'''\begin{center}
            \begin{tikzpicture}[scale='''+str(sc)+r''', font=\footnotesize, >=stealth]
                \draw[step=0.5, yellow!40, very thin] (0,0) grid ('''+str(a)+r''','''+str(a)+r''');
                \draw[thick] (0,0) node[below left]{$D$} -- ('''+str(a)+r''',0) node[below right]{$C$} 
                      -- ('''+str(a)+r''','''+str(a)+r''') node[above right]{$B$} 
                      -- (0,'''+str(a)+r''') node[above left]{$A$} -- cycle;
                \coordinate (E) at ('''+str(k1)+r''','''+str(a)+r''');
                \coordinate (F) at ('''+str(a)+r''','''+str(a-k2)+r''');
                \coordinate (G) at ('''+str(a-y_draw)+r''',0);
                \coordinate (H) at (0,'''+str(a-x_draw)+r''');
                \draw[thick, fill=blue!10, opacity=0.7] (E) -- (F) -- (G) -- (H) -- cycle;
                \foreach \p/\pos in {E/above, F/right, G/below, H/left}
                    \fill (\p) circle (2pt) node[\pos] {$\p$};
                \draw[<->] (0,'''+str(a+0.4)+r''') -- ('''+str(k1)+r''','''+str(a+0.4)+r''') node[midway, above] {$'''+str(k1)+r'''$ cm};
                \draw[<->] ('''+str(a+0.4)+r''','''+str(a)+r''') -- ('''+str(a+0.4)+r''','''+str(a-k2)+r''') node[midway, right] {$'''+str(k2)+r'''$ cm};
                \draw[<->] (-0.5,'''+str(a)+r''') -- (-0.5,'''+str(a-x_draw)+r''') node[midway, left] {$x$ cm};
                \draw[<->] ('''+str(a)+r''',-0.5) -- ('''+str(a-y_draw)+r''',-0.5) node[midway, below] {$y$ cm};
            \end{tikzpicture}
            \end{center}'''

                # ==========================================
                # BƯỚC 2: VIẾT LẠI NỘI DUNG CÂU HỎI VÀ LỜI GIẢI
                # ==========================================
                cauhoi_text = r'''Cho một tấm nhôm hình vuông cạnh $%s$ cm. Người ta muốn cắt một hình thang $EFGH$ như hình vẽ. Tổng $x + y$ để diện tích hình thang $EFGH$ đạt giá trị nhỏ nhất là''' % (latex(a))
                noidungcauhoi = cauhoi_text + tikz_code

                da_d = r'\True ' + str(kq)
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Lời giải chi tiết theo đúng logic ảnh
                loigiai = (r'''Ta có $S_{EFGH}$ nhỏ nhất $\Leftrightarrow  S = S_{AEH} + S_{FCG} + S_{GDH}$ lớn nhất. \\
                            Ta có: $2S = %sx + %sy + (%s-x)(%s-y) = xy - %sx - %sy + %s$ (1). \\
                            Mặt khác: $\triangle AEH \sim \triangle CGF$ nên $\frac{AE}{CG} = \frac{AH}{CF} \Rightarrow \frac{%s}{y} = \frac{x}{%s - %s} \Rightarrow xy = %s$ (2). \\
                            Từ (1) và (2) suy ra $2S = %s - \left( %sx + \frac{%s}{x} \right)$. \\
                            Ta có: $2S_{max} \Leftrightarrow  \left( %sx + \frac{%s}{x} \right)_{min}$. \\
                            Áp dụng bất đẳng thức Cô-si: $%sx + \frac{%s}{x} \ge 2\sqrt{%sx \cdot \frac{%s}{x}} = %s$. \\
                            Dấu "=" xảy ra khi $%sx = \frac{%s}{x} \Rightarrow x = %s \Rightarrow y = %s$. \\
                            Vậy $x + y = %s$.'''
                          % (latex(k1), latex(k2), latex(a), latex(a), latex(a-k1), latex(a-k2), latex(a*a),
                             latex(k1), latex(a), latex(k2), latex(const_xy),
                             latex(a*a + const_xy), latex(a-k1), latex((a-k2)*const_xy),
                             latex(a-k1), latex((a-k2)*const_xy),
                             latex(a-k1), latex((a-k2)*const_xy), latex(a-k1), latex((a-k2)*const_xy), 
                             latex(simplify(2*sqrt((a-k1)*(a-k2)*const_xy))),
                             latex(a-k1), latex((a-k2)*const_xy),
                             latex(x_val), latex(y_val), latex(tong_xy)
                            ))

            # ==========================================
            # XUẤT KẾT QUẢ
            # ==========================================
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\n\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

