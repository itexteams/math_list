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


def bt_dang10_p3_b1_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Sinh ngẫu nhiên các giá trị cho bài toán
                u1 = randint(-5, 5)
                u2 = randint(-5, 5)
                k = randint(1, 3)

                # Tính toán các số hạng kế tiếp theo công thức truy hồi: u_{n+1} = u_n + k * u_{n-1}
                u3 = u2 + k * u1
                u4 = u3 + k * u2
                u5 = u4 + k * u3

                kq = u5

                # Đáp án đúng
                du = ['$%s$' % (latex(kq))]
                da = random.choice(du)

                # Các đáp án sai ngẫu nhiên, không trùng với đáp án đúng
                s = [
                    '$%s$' % (latex(kq + 1)),
                    '$%s$' % (latex(kq - 1)),
                    '$%s$' % (latex(kq + 2)),
                    '$%s$' % (latex(kq - 2)),
                    '$%s$' % (latex(kq + 3)),
                    '$%s$' % (latex(kq - 3)),
                    '$%s$' % (latex(u4)),
                    '$%s$' % (latex(u3))
                ]

                # Lọc bỏ các giá trị trùng với đáp án đúng
                s = list(set([x for x in s if x != da]))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Tạo biểu thức công thức truy hồi
                if k == 1:
                    pt_rec = 'u_{n+1} = u_n + u_{n-1}'
                else:
                    pt_rec = 'u_{n+1} = u_n + %s u_{n-1}' % (latex(k))

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho dãy số $(u_n)$ xác định bởi $\\begin{cases} u_1 = %s, u_2 = %s \\\\ %s \\end{cases}$ với $n \\ge 2$. Số hạng thứ 5 của dãy bằng bao nhiêu?'''
                                 % (latex(u1), latex(u2), pt_rec))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết từng bước
                if k == 1:
                    step3 = '$u_3 = u_2 + u_1 = %s + (%s) = %s$' % (latex(u2), latex(u1), latex(u3))
                    step4 = '$u_4 = u_3 + u_2 = %s + (%s) = %s$' % (latex(u3), latex(u2), latex(u4))
                    step5 = '$u_5 = u_4 + u_3 = %s + (%s) = %s$' % (latex(u4), latex(u3), latex(u5))
                else:
                    step3 = '$u_3 = u_2 + %s u_1 = %s + %s \\cdot (%s) = %s$' % (latex(k), latex(u2), latex(k), latex(u1), latex(u3))
                    step4 = '$u_4 = u_3 + %s u_2 = %s + %s \\cdot (%s) = %s$' % (latex(k), latex(u3), latex(k), latex(u2), latex(u4))
                    step5 = '$u_5 = u_4 + %s u_3 = %s + %s \\cdot (%s) = %s$' % (latex(k), latex(u4), latex(k), latex(u3), latex(u5))

                loigiai = ('''Ta lần lượt tính các số hạng của dãy số:\\\\
                          - Với $n = 2$: %s.\\\\
                          - Với $n = 3$: %s.\\\\
                          - Với $n = 4$: %s.\\\\
                          Vậy số hạng thứ 5 của dãy bằng $%s$.'''
                           % (step3, step4, step5, latex(u5)))
            dapan='\\shortans[0]{$%s$}\n'%(latex(u5))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

