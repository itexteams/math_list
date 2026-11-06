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


def bt_dang41_p3_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            # Với a=5, b=3: 3(25-9) = 48. Các cặp (x, y) thỏa mãn y^2 - x^2 = 48 là (4, 8), (1, 7), (11, 13)
            danh_sach_bo_so = [
                {'a': 5, 'b': 3, 'x': 4, 'y': 8, 'sa': 9},
                {'a': 5, 'b': 3, 'x': 1, 'y': 7, 'sa': 6},
                {'a': 11, 'b': 7, 'x': 8, 'y': 16, 'sa': 12}
            ]

            sel = random.choice(danh_sach_bo_so)
            a_val, b_val, x_val, y_val, sa_val = sel['a'], sel['b'], sel['x'], sel['y'], sel['sa']

            # Tính toán các giá trị số thực (loại bỏ symbols/căn thức)
            ab_val = a_val * math.sqrt(3)
            bc_val = b_val * math.sqrt(3)
            ad_val = float(x_val)
            cd_val = float(y_val)
            sa_float = float(sa_val)

            # Diện tích đáy và Thể tích
            s_abcd = 0.5 * (ab_val * ad_val + bc_val * cd_val)
            v_abcd = (1/3) * sa_float * s_abcd

            # Tính BD và AH
            bd_val = math.sqrt(ab_val**2 + ad_val**2)
            ah_val = (ab_val * ad_val) / bd_val

            # Cotang góc SHA (Kết quả cuối cùng làm tròn đến hàng phần chục)
            cot_real = ah_val / sa_float
            da_dung_val = round(cot_real, 1)

            # Tạo các phương án nhiễu (Làm tròn 1 chữ số thập phân)
            da_dung = f"{da_dung_val:.1f}"
            sai1 = f"{round(bd_val / sa_float, 1):.1f}"
            sai2 = f"{round(sa_float / ah_val, 1):.1f}"
            sai3 = f"{round((a_val / sa_val) * math.sqrt(3), 1):.1f}"

            # Đảm bảo các phương án không trùng nhau một cách ngẫu nhiên nếu trùng
            options = list(set([da_dung, sai1, sai2, sai3]))
            while len(options) < 4:
                random_noise = round(da_dung_val + random.uniform(0.1, 1.0), 1)
                options.append(f"{random_noise:.1f}")
                options = list(set(options))

            list_da = [('\\True ' + da_dung)] + [opt for opt in options if opt != da_dung]
            random.shuffle(list_da)

            # Vẽ hình TikZ
            tikz_code = (r'''\begin{center}
                \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                    \draw [line width=1]    (92.47,168.4) -- (212.47,168.4) ;
                    \draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (164.47,150.4) -- (164.47,35.4) ;
                    \draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (132.47,128.4) -- (252.47,128.4) ;
                    \draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (92.47,168.4) -- (132.47,128.4) ;
                    \draw [line width=1]    (212.47,168.4) -- (252.47,128.4) ;
                    \draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (132.47,128.4) -- (164.47,150.4) ;
                    \draw [line width=1]    (164.47,35.4) -- (92.47,168.4) ; 
                    \draw [line width=1]    (164.47,35.4) -- (212.47,168.4) ;
                    \draw [line width=1]    (164.47,35.4) -- (252.47,128.4) ;
                    \draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (92.47,168.4) -- (252.47,128.4) ;
                    \draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (132.47,128.4) -- (164.47,35.4) ;
                    \draw (157,10) node [anchor=north west][inner sep=0.75pt]    {$S$};
                    \draw (118,111) node [anchor=north west][inner sep=0.75pt]    {$A$};
                    \draw (74,166) node [anchor=north west][inner sep=0.75pt]    {$B$};
                    \draw (212.47,168.4) node [anchor=north west][inner sep=0.75pt]    {$C$};
                    \draw (255.47,117.4) node [anchor=north west][inner sep=0.75pt]    {$D$};
                \end{tikzpicture}
            \end{center}''')

            # Nội dung câu hỏi (Làm tròn các giá trị đề bài cho đẹp)
            noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có $AB \\approx %s$, $BC \\approx %s$, góc $\\widehat{BAD} = \\widehat{BCD} = 90^\\circ$, $SA = %s$ và $SA$ vuông góc với đáy. Biết thể tích khối chóp $S.ABCD$ xấp xỉ bằng $%s$, cotang của góc giữa mặt phẳng $\\left(SBD\\right)$ và mặt đáy bằng (làm tròn đến hàng phần chục)'''
                            %(f"{ab_val:.1f}", f"{bc_val:.1f}", f"{sa_float:.1f}", f"{v_abcd:.1f}"))

            # Nội dung lời giải chi tiết
            loigiai = (f'''Có: $V_{{S.ABCD}} = \\frac{{1}}{{3}} \\cdot SA \\cdot S_{{ABCD}} \\Rightarrow S_{{ABCD}} = \\frac{{3V}}{{SA}} \\approx {s_abcd:.1f}$. \\\\
            Suy ra $\\frac{{1}}{{2}}AB \\cdot AD + \\frac{{1}}{{2}}BC \\cdot CD \\approx {s_abcd:.1f}$. \\\\
            Áp dụng định lí Pitago: $AB^2 + AD^2 = BC^2 + CD^2 \\Rightarrow CD^2 - AD^2 = AB^2 - BC^2$. \\\\
            Giải hệ phương trình ta được $AD = {ad_val:.1f}$ và $CD = {cd_val:.1f}$. \\\\
            Kẻ $AH \\perp BD$, góc cần tìm là $\\widehat{{SHA}}$. \\\\
            Tính được $BD = \\sqrt{{AB^2 + AD^2}} \\approx {bd_val:.1f}$, $AH = \\frac{{AB \\cdot AD}}{{BD}} \\approx {ah_val:.1f}$. \\\\
            $\\cot \\widehat{{SHA}} = \\frac{{AH}}{{SA}} = \\frac{{{ah_val:.1f}}}{{{sa_float:.1f}}} \\approx {da_dung}$.''')
            dapan='\\shortans[0]{$%s$}\n'%(str(da_dung).replace('.',','))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{'+ tikz_code+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

