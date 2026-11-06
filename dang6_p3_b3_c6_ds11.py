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


def bt_dang6_p3_b3_c6_ds11(self):
            # Khai báo biến
            # Khởi tạo các giá trị ngẫu nhiên
            khoi_dau = random.randint(1,20)
            do_dai = random.randint(7, 12)
            tu_so = random.randint(1, 8) if do_dai < 9 else random.randint(1, 6) if do_dai < 11 else random.randint(1, 3)
            bo_3 = []
            # Duyệt tất cả các bộ ba số a, b, c thoả điều kiện
            for a in range(khoi_dau, khoi_dau + do_dai):
                for b in range(a + 1, khoi_dau + do_dai):
                    for c in range(b + 1, khoi_dau + do_dai):
                        # Kiểm tra tính chẵn lẻ giống nhau
                        if (a % 2 == b % 2 == c % 2):
                            # Kiểm tra không phải cấp số cộng
                            if 2*b != a + c:
                                bo_3.append([a, b, c])

            tap_S = f"{latex(set(list(range(khoi_dau, khoi_dau + do_dai))))}".replace(',', ';')
            tikz_latex = f'''\\begin{{tikzpicture}}[scale=.8,
            main_node/.style={{circle, draw, font=\\sffamily, minimum size=20pt}}
            ]
            \\def\\r{{2}}
            \\path (90:\\r) coordinate (A)
            (210:\\r) coordinate (B)
            (-30:\\r) coordinate (C)
            ($(A)!1/2!(B)$) coordinate (M)
            ($(A)!1/2!(C)$) coordinate (P)
            ($(C)!1/2!(B)$) coordinate (N)
            ;
            \\draw (A) -- (M)--(B)--(N)--(C)--(P)--cycle; 
            % Đặt các node lên trên các đường đã vẽ để che đi phần giao nhau
            \\foreach \\x in {{A,B,C,M,N,P}} \\node[main_node,fill=yellow] at (\\x) {{$\\x$}} ;
            \\end{{tikzpicture}} '''
            ket_qua = S(tu_so * math.perm(do_dai, 6)) / (math.factorial(3) * len(bo_3))

            noidungcauhoi = f""" \\immini{{
                    Bạn Nam tham gia cuộc thi giải một mật thư. Theo quy tắc của cuộc thi, người chơi cần chọn ra sáu số từ tập hợp \\text{{$S = {tap_S}$}}
                    và xếp mỗi số vào đúng một vị trí trong sáu vị trí $A, B, C, M, N, P$ như hình bên.  
                    Mật thư sẽ được giải nếu các bộ ba số xuất hiện ở những bộ ba vị trí \\text{{$(A, M, B)$}}; \\text{{$(B, N, C)$}}; \\text{{$(C, P, A)$}} tạo thành các cấp số cộng theo thứ tự đó. 
                    Bạn Nam chọn ngẫu nhiên sáu số trong tập $S$ và xếp ngẫu nhiên vào các vị trí yêu cầu. 
                    Gọi xác suất để bạn Nam giải được mật thư ở lần chọn và xếp đó là $a$. 
                    Giá trị của $\\dfrac{{{tu_so}}}{{a}}$ bằng bao nhiêu?
                    }}{{{tikz_latex}}}"""
            loigiai = f"""Vì $\\begin{{cases}}
                        A + B = 2M\\\\ 
                        B + C = 2N\\\\ 
                        A + C = 2P 
                        \\end{{cases}} $ 
                        nên $A, B, C$ có cùng tính chẵn lẻ.\\\\
                        Có ${len(bo_3)}$ bộ ba số phù hợp xếp vào các vị trí $A, B, C$ là {'; '.join('$' + str(latex(set(tap))) + '$' for tap in bo_3)}.\\\\
                        Gọi $A$ là biến cố \\lq\\lq Nam giải được mật thư \\rq\\rq.\\\\
                        Hoán vị mỗi bộ ba số này ta được $n(A) = {len(bo_3)} \\times 3! = {len(bo_3) * math.factorial(3) }$.\\\\
                        Khi đó, xác suất bạn Nam giải được mật thư là $a = \\mathrm{{P}}(A) = \\dfrac{{{len(bo_3) * math.factorial(3) }}}{{\\mathrm{{A}}_{{{do_dai}}}^{{6}}}} = {latex(S(len(bo_3) * math.factorial(3)) / math.perm(do_dai, 6))}$.\\\\
                        Giá trị của $\\dfrac{{{tu_so}}}{{a}} = {latex(ket_qua)} $."""
            #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(latex(ket_qua))              

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('$zz$','.').replace('\\frac','\\dfrac')
            return content  

