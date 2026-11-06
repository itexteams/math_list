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


def bt_dang59_p1_b1_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            a = random.randint(2, 5)
            b = random.randint(1, 3)
            c = random.randint(2, 4)
            d = random.randint(1, 4)
            e = random.randint(1, 3)
            f = random.randint(2, 5)

            # Các đáp án trắc nghiệm
            da = '$u_n = \\frac{n^2 + %s}{%sn + %s}$' % (b, c, d)
            das1 = '$u_n = \\frac{n}{%s^n}$' % (a)
            das2 = '$u_n = \\frac{n}{%sn^2 + %s}$' % (e, f)
            das3 = '$u_n = (-%s)^n \\sqrt{n^2 - 1}$' % (a)

            # Câu hỏi
            noidungcauhoi = ('Trong các dãy số $(u_n)$ cho bởi số hạng tổng quát $u_n$ sau, dãy số nào tăng?')

            # Các đáp án
            da_d = ('\\True ' + str(da))
            da_s1 = str(das1)
            da_s2 = str(das2) 
            da_s3 = str(das3) 

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Tính toán các hệ số cho lời giải để tránh lỗi format string
            tu1_n3 = c
            tu1_n2 = d + 2*c
            tu1_n = 2*d + c*(b+1)
            tu1_c = d*(b+1)

            tu2_n3 = c
            tu2_n2 = c+d
            tu2_n = b*c
            tu2_c = b*(c+d)

            hieu_n2 = tu1_n2 - tu2_n2 
            hieu_n = tu1_n - tu2_n 
            hieu_c = tu1_c - tu2_c 

            # Xử lý dấu cho hệ số tự do để hiển thị LaTeX đẹp mắt
            if hieu_c > 0:
                chuoi_hieu_c = f"+ {hieu_c}"
            elif hieu_c < 0:
                chuoi_hieu_c = f"- {abs(hieu_c)}"
            else:
                chuoi_hieu_c = ""

            # Nội dung lời giải (Đã căn chỉnh khớp hoàn toàn số lượng %s)
            loigiai = ('Xét đáp án chứa dãy số có số hạng tổng quát: $u_n = \\frac{n^2 + %s}{%sn + %s}$.\\\\ '
                       'Ta xét hiệu $H = u_{n+1} - u_n = \\frac{(n+1)^2 + %s}{%s(n+1) + %s} - \\frac{n^2 + %s}{%sn + %s}$\\\\ '
                       '$= \\frac{n^2 + 2n + %s}{%sn + %s} - \\frac{n^2 + %s}{%sn + %s} = \\frac{(n^2 + 2n + %s)(%sn + %s) - (n^2 + %s)(%sn + %s)}{(%sn + %s)(%sn + %s)}$.\\\\ '
                       'Khai triển tử số:\\\\ '
                       '$(n^2 + 2n + %s)(%sn + %s) = %sn^3 + %sn^2 + %sn + %s$.\\\\ '
                       '$(n^2 + %s)(%sn + %s) = %sn^3 + %sn^2 + %sn + %s$.\\\\ '
                       'Hiệu tử số bằng: $%sn^2 + %sn %s$.\\\\ '
                       'Vì $n \\in \\mathbb{N}^*$ nên dễ thấy tử số luôn dương với mọi $n \\ge 1$.\\\\ '
                       'Mẫu số bằng $(%sn + %s)(%sn + %s) > 0$. Do đó $H > 0$. Vậy $(u_n)$ là dãy số tăng.'
                       %(b, c, d, 
                         b, c, d, b, c, d, 
                         b+1, c, c+d, b, c, d, b+1, c, d, b, c, c+d, c, c+d, c, d,
                         b+1, c, d, tu1_n3, tu1_n2, tu1_n, tu1_c,
                         b, c, c+d, tu2_n3, tu2_n2, tu2_n, tu2_c,
                         hieu_n2, hieu_n, chuoi_hieu_c,
                         c, c+d, c, d))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

