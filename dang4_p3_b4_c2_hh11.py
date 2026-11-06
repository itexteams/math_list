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


def bt_dang4_p3_b4_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random chiều rộng cửa (BN)
                widths = [1.2, 1.4, 1.5, 1.6, 1.8]
                bn_val = random.choice(widths)

                # Kết quả AN = BN (do tam giác ABN đều khi góc mở = 60 độ)
                ans_val = bn_val

                # Hàm xử lý định dạng số: đổi dấu chấm thành phẩy
                def format_num(num):
                    s = str(num).replace('.', ',')
                    if s.endswith(',0'):
                        s = s[:-2]
                    return s

                kq = format_num(ans_val)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Tạo các phương án sai ngẫu nhiên
                wrong_offsets = [0.1, -0.1, 0.2, -0.2, 0.3, -0.3]
                s_list = []
                for offset in wrong_offsets:
                    w_val = round(ans_val + offset, 1)
                    if w_val > 0 and w_val != ans_val:
                        s_list.append('$%s$' % format_num(w_val))

                # Thêm các đáp án sai dễ gây nhầm lẫn (cạnh nhân căn 2, căn 3)
                s_list.append('$%s\\sqrt{2}$' % format_num(ans_val))
                s_list.append('$%s\\sqrt{3}$' % format_num(ans_val))

                # Lọc trùng và lấy ngẫu nhiên 3 phương án sai
                s_list = list(set(s_list))
                random.shuffle(s_list)
                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Vẽ lại mô hình bằng TikZ
                tikz_code = ('\\begin{center}\n'
                '\\begin{tikzpicture}[line width=1pt]\n'
                '    \\coordinate (D) at (0,2);\n'
                '    \\coordinate (C) at (3,2);\n'
                '    \\coordinate (A) at (0,0);\n'
                '    \\coordinate (B) at (3,0);\n'
                '    \\coordinate (M) at (0.55, 1.5);\n'
                '    \\coordinate (N) at (0.55,-0.5);\n'
                '    \\draw (-1.5, 0.5) -- (0, 0.5);\n'
                '    \\draw (3, 0.5) -- (4.5, 0.5);\n'
                '    \\draw (-1.5, -1.2) -- (4.5, -1.2);\n'
                '    \\draw[blue] (D) -- (C);\n'
                '    \\draw[blue] (D) -- (A) -- (B);\n'
                '    \\draw[fill=pink!60!white, draw=black!80!red, thick] (N) -- (B) -- (C) -- (M) -- cycle;\n'
                '    \\fill (D) circle (1.5pt) node[left] {$D$};\n'
                '    \\fill (C) circle (1.5pt) node[right] {$C$};\n'
                '    \\fill (A) circle (1.5pt) node[left] {$A$};\n'
                '    \\fill (B) circle (1.5pt) node[right] {$B$};\n'
                '    \\fill (M) circle (1.5pt) node[below right, yshift=2pt] {$M$};\n'
                '    \\fill (N) circle (1.5pt) node[below] {$N$};\n'
                '\\end{tikzpicture}\n'
                '\\end{center}')

                # Câu hỏi
                noidungcauhoi = ('''Hình bên dưới minh họa một cánh cửa và khung cửa. Cánh cửa có dạng hình chữ nhật $BCMN$ và khung cửa có dạng hình chữ nhật $ABCD$ và biết được $AB = BN$. Góc mở cửa là góc nhị diện $[A, BC, N]$. Biết chiều rộng $BN$ của cửa là $%s$ mét. Khi góc mở cửa bằng $60^\\circ$ thì khoảng cách giữa $A$ và $N$ bằng bao nhiêu?\n%s''' 
                                 % (kq, tikz_code))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Vì $AB \\perp BC$ và $NB \\perp BC$ nên góc $\\widehat{ABN}$ là góc phẳng nhị diện của góc nhị diện $[A, BC, N]$. \\\\
            Vì góc mở cửa bằng $60^\\circ$ nên số đo góc nhị diện $[A, BC, N]$ bằng $60^\\circ$ suy ra $\\widehat{ABN} = 60^\\circ$. \\\\
            Xét tam giác $ABN$ cân tại $B$ có: $BA = BN = %s$ m và $\\widehat{ABN} = 60^\\circ$. \\\\
            Khi đó $\\Delta ABN$ là tam giác đều suy ra $AN = %s$ m hay khoảng cách giữa $A$ và $N$ bằng $%s$ m.'''
                           % (kq, kq, kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content       

