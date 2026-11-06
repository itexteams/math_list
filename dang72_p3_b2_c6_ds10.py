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


def bt_dang72_p3_b2_c6_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # n là tổng số nút trên vòng tròn (chẵn, n >= 8)
        # k là số nút cần chọn sao cho không có 2 nút cạnh nhau: 2*k <= n
        list_cases = [(8, 3), (10, 3), (10, 4), (12, 4), (12, 5)]
        n, k = random.choice(list_cases)
        doi_dien = 1 + n // 2

        # Không gian mẫu: Số cách chọn k nút từ n nút
        omega = math.comb(n, k)

        # Số cách chọn k phần tử không kề nhau trên vòng tròn n phần tử:
        c_n_minus_k_k = math.comb(n - k, k)
        c_n_minus_k_minus_1_k_minus_1 = math.comb(n - k - 1, k - 1)
        n_circle = (n * c_n_minus_k_k) // (n - k)

        # Đếm số cách chọn k nút không kề nhau mà CẢ HAI NÚT 1 và doi_dien đều được chọn:
        m = doi_dien
        len1 = m - 4
        len2 = n - m - 2

        def count_line(L, r):
            if r < 0 or r > L:
                return 0
            if L - r + 1 < r:
                return 0
            return math.comb(L - r + 1, r)

        n_both = 0
        for r1 in range(k - 1):
            r2 = (k - 2) - r1
            n_both += count_line(len1, r1) * count_line(len2, r2)

        # Số cách chọn biến cố A:
        n_A = n_circle - n_both

        # Xác suất P = n_A / omega
        P = Rational(n_A, omega)
        P_float = float(P)

        # Làm tròn số thập phân đến hàng phần chục
        number = Decimal(str(P_float))
        kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        P_latex = latex(P)

        # Tạo code TikZ minh họa hệ thống n nút trên đường tròn
        nodes_tikz = []
        for i in range(1, n + 1):
            # Góc phân bố theo chiều kim đồng hồ bắt đầu từ đỉnh trên cùng (90 độ)
            angle = 90 - (i - 1) * (360 / n)
            nodes_tikz.append('\\coordinate (N%d) at (%.2f:1.8);' % (i, angle))
            nodes_tikz.append('\\fill[black] (N%d) circle (1pt) node[anchor=%.2f] {$%d$};' % (i, angle + 180, i))

        tikz_nodes_str = '\n        '.join(nodes_tikz)

        hinhve = ('''\\begin{center}
            \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\draw[line width=1pt, black] (0,0) circle (1.8);
            %s
            \\end{tikzpicture}
            \\end{center}''' % (tikz_nodes_str))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một hệ thống quản lý điện lưới thông minh gồm $%s$ nút vận hành được bố trí thành một vòng tròn khép kín và được đánh số thứ tự liên tiếp từ $1$ đến $%s$ theo chiều kim đồng hồ như hình vẽ dưới đây:
    %s
    Để tiến hành bảo trì định kỳ, kỹ sư cần chọn ngẫu nhiên $%s$ nút để kích hoạt chế độ kiểm tra. Để đảm bảo an toàn tải điện, không có $2$ nút nào được kích hoạt nằm cạnh nhau trên vòng tròn. Đồng thời, do đặc tính kỹ thuật, nút $1$ và nút $%s$ (hai nút đối diện) không được phép kích hoạt cùng một lúc. Xác suất để chọn được tập hợp $%s$ nút thỏa mãn các điều kiện an toàn trên bằng bao nhiêu? (kết quả làm tròn đến hàng phần chục).'''
                         % (str(n), str(n), hinhve, str(k), str(doi_dien), str(k)))

        # Nội dung lời giải
        loigiai = ('''Không gian mẫu là số cách chọn ngẫu nhiên $%s$ nút từ $%s$ nút của hệ thống: \\\\
    $n(\\Omega) = \\mathrm{C}_{%s}^{%s} = %s$. \\\\
    Gọi $A$ là biến cố: "Chọn được $%s$ nút thỏa mãn không có $2$ nút nào cạnh nhau trên vòng tròn và không đồng thời chọn cả hai nút $1$ và $%s$". \\\\
    Bước 1: Số cách chọn $%s$ nút trong đó không có $2$ nút nào cạnh nhau trên vòng tròn $%s$ nút. \\\\
    Ta xét hai trường hợp: \\\\
    - Trường hợp 1: Không chọn nút $1$. Khi đó ta chọn $%s$ nút từ hàng ngang $%s$ nút còn lại $\\{2, 3, \\dots, %s\\}$ sao cho không có hai nút nào cạnh nhau. Số cách chọn là $\\mathrm{C}_{%s - %s + 1}^{%s} = \\mathrm{C}_{%s}^{%s} = %s$. \\\\
    - Trường hợp 2: Có chọn nút $1$. Do không chọn hai nút cạnh nhau nên nút $2$ và nút $%s$ không được chọn. Ta cần chọn $%s$ nút từ $%s$ nút $\\{3, 4, \\dots, %s\\}$ sao cho không có hai nút nào cạnh nhau. Số cách chọn là $\\mathrm{C}_{%s - %s + 1}^{%s} = \\mathrm{C}_{%s}^{%s} = %s$. \\\\
    Do đó, tổng số cách chọn $%s$ nút không có $2$ nút nào cạnh nhau trên vòng tròn là: \\\\
    $N_0 = %s + %s = %s$. \\\\
    Bước 2: Số cách chọn $%s$ nút không kề nhau mà đồng thời chọn cả hai nút $1$ và $%s$. \\\\
    Khi chọn nút $1$ và nút $%s$, các nút kề với chúng gồm $2, %s, %s, %s$ đều không được chọn. \\\\
    Các nút còn lại chia thành hai nhóm riêng biệt: \\\\
    + Nhóm 1 gồm các nút từ $3$ đến $%s$ (gồm $%s$ nút). \\\\
    + Nhóm 2 gồm các nút từ $%s$ đến $%s$ (gồm $%s$ nút). \\\\
    Cần chọn thêm $%s$ nút từ hai nhóm này sao cho trong mỗi nhóm không có hai nút kề nhau. Số cách chọn thỏa mãn là $%s$ cách. \\\\
    Bước 3: Số phần tử của biến cố $A$ là: \\\\
    $n(A) = %s - %s = %s$. \\\\
    Xác suất của biến cố $A$ là: \\\\
    $\\mathrm{P}(A) = \\frac{n(A)}{n(\\Omega)} = \\frac{%s}{%s} = %s \\approx %s$.'''
                   % (str(k), str(n),
                      str(n), str(k), str(omega),
                      str(k), str(doi_dien),
                      str(k), str(n),
                      str(k), str(n - 1), str(n), str(n - 1), str(k), str(k), str(n - k), str(k), str(c_n_minus_k_k),
                      str(n), str(k - 1), str(n - 3), str(n - 1), str(n - 3), str(k - 1), str(k - 1), str(n - k - 1), str(k - 1), str(c_n_minus_k_minus_1_k_minus_1),
                      str(k),
                      str(c_n_minus_k_k), str(c_n_minus_k_minus_1_k_minus_1), str(n_circle),
                      str(k), str(doi_dien),
                      str(doi_dien), str(n), str(doi_dien - 1), str(doi_dien + 1),
                      str(doi_dien - 2), str(len1),
                      str(doi_dien + 2), str(n - 1), str(len2),
                      str(k - 2), str(n_both),
                      str(n_circle), str(n_both), str(n_A),
                      str(n_A), str(omega), P_latex, kq_str
                      ))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content

