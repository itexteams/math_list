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


def bt_dang70_p3_b2_c6_ds10(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Random số lượng phần tử của tập X (chọn các bội của 3 để đảm bảo bài toán có nghiệm đẹp)
        n = random.choice([9, 12, 15, 18, 21])
        k = n // 3

        # Tính không gian mẫu
        khong_gian_mau = math.comb(n, 4) * 4

        # Tính số kết quả thuận lợi
        so_kq_thuan_loi = 0
        cases_str = ""
        for b in range(2, k + 1):
            d = 3 * b
            pairs = b - 1
            so_kq_thuan_loi += pairs
            cases_str += "Với $b=%s \\Rightarrow d=%s$, có $%s$ cặp $(a; c)$ thỏa mãn $a+c=%s$.\\\\" % (b, d, pairs, 2*b)

        # Rút gọn phân số xác suất P
        P_fraction = frac(so_kq_thuan_loi, khong_gian_mau)
        tu_so = P_fraction.numerator
        mau_so = P_fraction.denominator

        # Random hệ số K nhân với P để ra kết quả số nguyên
        kq_int = random.randint(50, 150)
        HeSo = (kq_int * mau_so) // tu_so

        kq = kq_int

        # Các đáp án trắc nghiệm
        du = ['$%s$'%(kq)]
        da = random.choice(du)
        s = ['$%s$'%(kq + 1),
             '$%s$'%(kq + 2),
             '$%s$'%(kq + 3),
             '$%s$'%(kq - 1),
             '$%s$'%(kq - 2),
             '$%s$'%(kq - 3)]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Code vẽ hình TikZ
        tikz_str = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt] (0,0) circle (0.7);
        \\draw[line width=1pt] (0,1.8) circle (0.5);
        \\draw[line width=1pt] (-1.5,-1) circle (0.5);
        \\draw[line width=1pt] (1.5,-1) circle (0.5);
        \\draw[line width=1pt, dashed] (0,0.7) -- (0,1.3);
        \\draw[line width=1pt, dashed] (-0.6,-0.4) -- (-1.1,-0.7);
        \\draw[line width=1pt, dashed] (0.6,-0.4) -- (1.1,-0.7);
    \\end{tikzpicture}
    \\end{center}''')

        # Câu hỏi
        noidungcauhoi = ('''Cho tập hợp $X = \\{1; 2; 3; \\ldots; %s\\}$. Chọn ngẫu nhiên $4$ số phân biệt từ tập $X$. Trong $4$ số được chọn, ta đặt $1$ số vào vòng tròn lớn ở chính giữa, $3$ số còn lại được đặt vào ba vòng tròn nhỏ xung quanh (biết rằng ba vòng tròn nhỏ này không phân biệt vị trí).
    %s
    Gọi $P$ là xác suất để các số được đặt thỏa mãn đồng thời hai điều kiện sau:
    - Ba số ở ba vòng tròn nhỏ có thể sắp xếp thành một cấp số cộng tăng.
    - Số ở vòng tròn lớn chính giữa bằng tổng của cả ba số ở ba vòng tròn nhỏ.
    Giá trị của biểu thức $%s P$ bằng bao nhiêu?'''
                         %(latex(n), tikz_str, latex(HeSo)))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Số phần tử của không gian mẫu: Chọn $4$ số từ tập $X$ có $\\mathrm{C}_{%s}^4$ cách. Chọn $1$ số trong $4$ số đó đặt vào vòng tròn lớn có $4$ cách. $3$ số còn lại đặt vào $3$ vòng tròn nhỏ không phân biệt vị trí có $1$ cách. \\\\
    Do đó $n(\\Omega) = 4 \\cdot \\mathrm{C}_{%s}^4 = %s$.\\\\
    Gọi biến cố $A$: "Các số được đặt thỏa mãn điều kiện".\\\\
    Gọi $3$ số ở $3$ vòng tròn nhỏ là $a, b, c$ ($1 \\le a < b < c \\le %s$). Theo giả thiết ta có $a, b, c$ lập thành cấp số cộng nên $a+c=2b$.\\\\
    Số ở vòng tròn lớn là $d = a+b+c = 3b$.\\\\
    Vì $d \\in X$ nên $3b \\le %s \\Leftrightarrow b \\le %s$. Mà $b \\ge 2$ nên $b \\in \\{2; 3; \\ldots; %s\\}$.\\\\
    %s
    Vậy số kết quả thuận lợi cho biến cố $A$ là $n(A) = %s$.\\\\
    Xác suất cần tìm là $P = \\frac{n(A)}{n(\\Omega)} = \\frac{%s}{%s} = \\frac{%s}{%s}$.\\\\
    Giá trị biểu thức $%s P = %s \\cdot \\frac{%s}{%s} = %s$.'''
                   %(latex(n), latex(n), latex(khong_gian_mau), 
                     latex(n), latex(n), latex(k), latex(k),
                     cases_str,
                     latex(so_kq_thuan_loi), 
                     latex(so_kq_thuan_loi), latex(khong_gian_mau), latex(tu_so), latex(mau_so),
                     latex(HeSo), latex(HeSo), latex(tu_so), latex(mau_so), latex(kq)))
    dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) +dapan+
               '\\loigiai{\n' + str(loigiai) + '\n}\n'
               '\\end{ex}\n\\end{minipage} \n\n')
    return content

