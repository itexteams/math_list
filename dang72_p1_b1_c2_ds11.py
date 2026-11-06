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


def bt_dang72_p1_b1_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random hệ số cho đáp án đúng d_n
                A_d = randint(2, 6)
                B_d = randint(2, 5)

                # Random hệ số cho các đáp án sai a_n, b_n, c_n
                A_a = randint(1, 5)
                A_b = randint(1, 5)
                B_b = randint(2, 5)
                A_c = randint(2, 4)
                B_c = randint(2, 5)

                # Chuẩn hóa chuỗi hiển thị tránh số 1 đứng trước biến
                a_term = "%sn" % A_a if A_a > 1 else "n"
                b_num = str(A_b)
                b_den = "%sn" % B_b if B_b > 1 else "n"

                # Các đáp án
                da_d_text = "Dãy $(d_n)$, với $d_n = \\frac{%sn}{n^3 + %s}, \\forall n \\in \\mathbb{N}^*$" % (A_d, B_d)
                da_a_text = "Dãy $(a_n)$, với $a_n = \\sqrt{n^3 + %s}, \\forall n \\in \\mathbb{N}^*$" % (a_term)
                da_b_text = "Dãy $(b_n)$, với $b_n = n^2 + \\frac{%s}{%s}, \\forall n \\in \\mathbb{N}^*$" % (b_num, b_den)
                da_c_text = "Dãy $(c_n)$, với $c_n = (-%s)^n + %s, \\forall n \\in \\mathbb{N}^*$" % (A_c, B_c)

                # Câu hỏi
                noidungcauhoi = ('%s' % ('Trong các dãy số sau dãy số nào bị chặn ?'))

                # Các đáp án trắc nghiệm
                da_d = ('\\True ' + da_d_text)
                list_s = [da_a_text, da_b_text, da_c_text]
                random.shuffle(list_s)

                da_s1 = list_s[0]
                da_s2 = list_s[1]
                da_s3 = list_s[2]

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Ta xét tính bị chặn của các dãy số: \\\\
            - Với dãy $(a_n)$: $\\lim a_n = \\lim \\sqrt{n^3 + %s} = +\\infty$ nên dãy $(a_n)$ không bị chặn trên. \\\\
            - Với dãy $(b_n)$: $\\lim b_n = \\lim \\left(n^2 + \\frac{%s}{%s}\\right) = +\\infty$ nên dãy $(b_n)$ không bị chặn trên. \\\\
            - Với dãy $(c_n)$: $\\lim |c_n| = \\lim |(-%s)^n + %s| = +\\infty$ nên dãy $(c_n)$ không bị chặn. \\\\
            - Với dãy $(d_n)$: Ta có $d_n = \\frac{%sn}{n^3 + %s} > 0, \\forall n \\in \\mathbb{N}^*$, suy ra dãy bị chặn dưới. \\\\
            Mặt khác, $n^3 + %s > n^3 \\Rightarrow \\frac{1}{n^3 + %s} < \\frac{1}{n^3} \\Rightarrow d_n = \\frac{%sn}{n^3 + %s} < \\frac{%sn}{n^3} = \\frac{%s}{n^2} \\le %s, \\forall n \\in \\mathbb{N}^*$. \\\\
            Do đó $0 < d_n \\le %s, \\forall n \\in \\mathbb{N}^*$, suy ra dãy $(d_n)$ bị chặn.'''
                           % (a_term, b_num, b_den, A_c, B_c, A_d, B_d, B_d, B_d, A_d, B_d, A_d, A_d, A_d, A_d))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

