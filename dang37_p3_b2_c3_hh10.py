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


def bt_dang37_p3_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # d1: ax + by + c = 0
                # d2: x = x0 + u1*t, y = y0 + u2*t
                # Để đơn giản và số đẹp, ta chọn các thông số sao cho t và x_A là số nguyên

                # Random d2 sao cho giao điểm với Ox (y=0) có t nguyên
                u2 = randint(1, 5) * random.choice([-1, 1])
                t_inter = randint(-5, 5)
                # y = y0 + u2*t = 0 => y0 = -u2 * t_inter
                y0 = -u2 * t_inter

                x0 = randint(-5, 5)
                u1 = randint(1, 5) * random.choice([-1, 1])

                # Tọa độ giao điểm A trên Ox: y_A = 0
                x_A = x0 + u1 * t_inter

                # Đảm bảo x_A khác 0 để tìm được a duy nhất (ax_A + c = 0)
                while x_A == 0:
                    x0 = randint(-5, 5)
                    x_A = x0 + u1 * t_inter

                # Random thông số d1: ax + by + c = 0
                b = randint(1, 5)
                # a*x_A + b*0 + c = 0 => c = -a*x_A. Ta chọn a trước để có kết quả đẹp.
                kq_a = randint(-5, 5)
                while kq_a == 0: kq_a = randint(-5, 5)

                c = -kq_a * x_A

                # Các giá trị để đưa vào latex
                val_a = kq_a
                val_b = b
                val_c = c
                val_x0 = x0
                val_u1 = u1
                val_y0 = y0
                val_u2 = u2

                # Đáp án đúng
                da = '$a = %s$' % (latex(val_a))

                # Tạo các phương án sai
                s = set()
                while len(s) < 3:
                    sai = kq_a + random.choice([-2, -1, 1, 2, 3])
                    if sai != kq_a:
                        s.add('$a = %s$' % (latex(sai)))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                # Viết phương trình d1: ax + by + c = 0 -> xử lý dấu của c
                sign_c = "+" if val_c >= 0 else ""
                pt_d1 = "ax + %sy %s %s = 0" % (latex(val_b), sign_c, latex(val_c))

                noidungcauhoi = ("Giá trị của $a$ để hai đường thẳng $d_1: %s$ và $d_2: \\begin{cases} x = %s + %st \\\\ y = %s + %st \\end{cases}$ cắt nhau tại một điểm nằm trên trục hoành bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)."
                                 % (pt_d1, latex(val_x0), latex(val_u1), latex(val_y0), latex(val_u2)))

                # Các đáp án
                da_d = '\\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                h1=val_a
                number = Decimal(float(h1))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kqz=str(kq1).replace('.',',')

                loigiai = ("Gọi $A$ là giao điểm của hai đường thẳng $d_1$ và $d_2$. \\\\ "
                           "Vì $A$ nằm trên trục hoành nên tung độ của $A$ bằng $0$, tức là $y_A = 0$. \\\\ "
                           "Thay $y = 0$ vào phương trình tham số của $d_2$, ta có: \\\\ "
                           "$%s + %st = 0 \\Leftrightarrow %st = %s \\Leftrightarrow t = %s$. \\\\ "
                           "Với $t = %s$, thay vào phương trình $x = %s + %st$ ta được: \\\\ "
                           "$x = %s + %s(%s) = %s$. \\\\ "
                           "Suy ra tọa độ giao điểm là $A(%s; 0)$. \\\\ "
                           "Vì $A \\in d_1$ nên ta có: \\\\ "
                           "$a(%s) + %s(0) %s %s = 0 \\Leftrightarrow %sa %s %s = 0 \\Leftrightarrow a = %s$."
                           % (latex(val_y0), latex(val_u2), latex(val_u2), latex(-val_y0), latex(t_inter),
                              latex(t_inter), latex(val_x0), latex(val_u1),
                              latex(val_x0), latex(val_u1), latex(t_inter), latex(x_A),
                              latex(x_A),
                              latex(x_A), latex(val_b), sign_c, latex(val_c), latex(x_A), sign_c, latex(val_c), latex(val_a)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(kqz)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 


