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


def bt_dang53_p4_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo danh sách dạng
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # k là chỉ số hệ số cần tìm (a_k)
                # m là số mũ cao nhất của đa thức
                k = random.randint(7, 10)
                m = k + random.randint(4, 6)

                # Tính toán kết quả chính xác dựa trên công thức tổng các tổ hợp: 
                # C(k,k) + C(k+1,k) + ... + C(m,k) = C(m+1, k+1)
                kq_val = sp.binomial(m + 1, k + 1)
                da_dung = '$%s$' % (latex(kq_val))

                # Bước 4: Điều chỉnh các phương án sai không trùng với đáp án đúng
                s = []
                while len(s) < 3:
                    sai = kq_val + random.choice([-100, -50, 50, 100, 200, -10, 10]) + random.randint(1, 20)
                    if sai != kq_val and sai > 0:
                        str_sai = '$%s$' % (latex(sai))
                        if str_sai not in s:
                            s.append(str_sai)

                das1, das2, das3 = s[0], s[1], s[2]

                # Câu hỏi
                # B2: Viết lại y hệt bài toán theo mẫu code
                noidungcauhoi = ('Cho đa thức $P\\left(x\\right) = \\left(1 + x\\right)^{%s} + \\left(1 + x\\right)^{%s} + \\dots + \\left(1 + x\\right)^{%s}$ có dạng khai triển là: $P\\left(x\\right) = a_0 + a_1x + a_2x^2 + \\dots + a_{%s}x^{%s}$. Hãy tính hệ số $a_{%s}$.'
                                 % (latex(k), latex(k+1), latex(m), latex(m), latex(m), latex(k)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                # Tạo chuỗi tổng các tổ hợp cho phần lời giải
                tong_to_hop = ' + '.join(['C_{%s}^{%s}' % (latex(i), latex(k)) for i in range(k, m + 1)])

                loigiai = ('Để tính hệ số $a_{%s}$ là hệ số của $x^{%s}$ ta tính hệ số $a_{%s}$ trong từng nhị thức của $P\\left(x\\right)$ rồi tính tổng của chúng. \\\\ '
                           'Xét khai triển $\\left(1 + x\\right)^{%s} = \\sum_{i=0}^{%s} C_{%s}^i x^i$. \\\\ '
                           'Hệ số của $x^{%s}$ trong khai triển trên tương ứng $i = %s$ là $C_{%s}^{%s}$. \\\\ '
                           'Xét khai triển $\\left(1 + x\\right)^{%s} = \\sum_{i=0}^{%s} C_{%s}^i x^i$. \\\\ '
                           'Hệ số của $x^{%s}$ trong khai triển trên tương ứng $i = %s$ là $C_{%s}^{%s}$. \\\\ '
                           'Thực hiện tương tự cho các nhị thức còn lại trong $P\\left(x\\right)$ ta được: \\\\ '
                           '$a_{%s} = %s = %s$.'
                           % (latex(k), latex(k), latex(k),
                              latex(k), latex(k), latex(k), latex(k), latex(k), latex(k), latex(k),
                              latex(k+1), latex(k+1), latex(k+1), latex(k), latex(k), latex(k+1), latex(k),
                              latex(k), tong_to_hop, latex(kq_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

