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


def bt_dang11_p3_b2_c2_hh12(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # === Tham số Random ===

                # 1. Random vectơ và Giao điểm A

                # vectơ chỉ phương của d: uD
                uD_options = [(1, -2, 2), (2, 1, -1), (1, 1, 2)]
                uD_tuple = random.choice(uD_options)
                uD = Matrix(uD_tuple)
                uDx, uDy, uDz = uD_tuple

                # vectơ pháp tuyến của P: nP (Để uDelta đẹp, ta chọn nP sau)

                # Giao điểm A = (P) giao d. Chọn A là điểm đi qua của d (t0=0)
                xA, yA, zA = randint(-5, -2), randint(2, 5), randint(-5, -2)

                # vectơ chỉ phương của Delta: uDelta (Phải vuông góc với nP và uD)
                # Chọn uDelta đơn giản:
                uDelta_options = [(2, 2, -2), (2, 3, 4), (-3, 2, -5)] 
                uDelta_tuple = random.choice(uDelta_options) 
                uDelta = Matrix(uDelta_tuple)
                uDeltax, uDeltay, uDeltaz = uDelta_tuple

                # nP = [uDelta, uD]
                nP = uDelta.cross(uD) 
                nPx, nPy, nPz = nP[0], nP[1], nP[2]

                # Phương trình mặt phẳng (P) đi qua A
                # nPx(x - xA) + nPy(y - yA) + nPz(z - zA) = 0
                D_mp = -(nPx*xA + nPy*yA + nPz*zA)

                # 2. Random t_I và tính y_I mới
                t_I_options = [-2, 2, 3, -3]  
                t_I = random.choice(t_I_options)

                # y_I là tọa độ được biết trước của I
                yI = yA + t_I * uDeltay 

                # 3. Tính a và b
                a = xA + uDeltax * t_I 
                b = zA + uDeltaz * t_I 

                # === Kết quả cuối cùng ===
                kq_num = a**2 + b**2
                kq = latex(kq_num)

                # === Tạo Đáp án Trắc nghiệm ===
                da = '$%s$' % kq
                s_nums = [kq_num + 1, kq_num - 1, kq_num + 5]
                random.shuffle(s_nums)
                s = ['$%s$' % latex(n) for n in s_nums]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)
                choice_options = '\n'.join('{' + str(item) + '}' for item in list_1)

                # Câu hỏi
                noidungcauhoi = ('''Trong không gian $Oxyz$, cho mặt phẳng $(P): %s x + %s y + %s z+%s = 0$ và đường thẳng $d: \\frac{x -%s}{%s} = \\frac{y -%s}{%s} = \\frac{z -%s}{%s}$. Gọi $\\Delta$ là đường thẳng nằm trong $(P)$, cắt và vuông góc với $d$. Biết điểm $I(a; %s; b) \\in \\Delta$. Giá trị $a^2+b^2$ bằng bao nhiêu?'''
                                 % (latex(nPx), latex(nPy), latex(nPz), ('+' + latex(Abs(D_mp)) if D_mp > 0 else ('' if D_mp == 0 else latex(D_mp))),
                                    latex(xA), latex(uDx), latex(yA), latex(uDy), latex(zA), latex(uDz),
                                    latex(yI)
                                 ))



                # Nội dung lời giải
                loigiai = ('''Mặt phẳng $(P)$ có VTPT $\\vec{n}_P=(%s; %s; %s)$. \\\\
                           Đường thẳng $d$ có VTCP $\\vec{u}_d=(%s; %s; %s)$ và đi qua $A(%s; %s; %s)$. \\\\
                VTCP của $\\Delta$: $\\vec{u}_{\\Delta} = [\\vec{n}_P, \\vec{u}_d] = (%s; %s; %s)$. \\\\
                Kiểm tra $A$ là giao điểm $(P) \\cap d$: $A$ thỏa mãn phương trình $(P)$ và thuộc $d$. Giao điểm là $A(%s; %s; %s)$. \\\\
                PTTS của $\\Delta$ đi qua $A(%s, %s, %s)$ là $\\begin{cases} x = %s+%st \\\\ y = %s+%st \\\\ z = %s+%st \\end{cases}$. \\\\
                Điểm $I(a; %s; b) \\in \\Delta$. Thay tọa độ $y_I = %s$ vào $\\Delta$:\\\\
                $$%s = %s + %st \\Rightarrow  t = %s.$$\\\\
                Với $t = %s$, ta tìm được $a$ và $b$:\\\\
                $$a = %s+%s \\cdot (%s) = %s$$
                $$b = %s+%s \\cdot (%s) = %s$$
                Vậy $a^2+b^2 = (%s)^2 + (%s)^2 = %s.$
                ''' % (latex(nPx), latex(nPy), latex(nPz), latex(uDx), latex(uDy), latex(uDz), latex(xA), latex(yA), latex(zA),
                       latex(uDeltax), latex(uDeltay), latex(uDeltaz), latex(xA), latex(yA), latex(zA),
                       latex(xA), latex(yA), latex(zA), 
                       latex(xA), latex(uDeltax), latex(yA), latex(uDeltay), latex(zA), latex(uDeltaz),
                       latex(yI), latex(yI),
                       latex(yI), latex(yA), latex(uDeltay), latex(t_I),
                       latex(t_I),
                       latex(xA), latex(uDeltax), latex(t_I), latex(a),
                       latex(zA), latex(uDeltaz), latex(t_I), latex(b),
                       latex(a), latex(b), kq
                         )
                         )
                # Đáp án ngắn
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_num))

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-').replace('+ -', '-').replace('--', '+').replace('++', '+')
            return content   

