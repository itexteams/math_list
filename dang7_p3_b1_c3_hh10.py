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


def bt_dang7_p3_b1_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập các hệ số cho đường thẳng Delta: Ax + By + C = 0
                # Trong đề bài mẫu A = 2, B = -1, C = 1
                A = 2 
                B = random.randint(-5, 5)
                while B == 0:
                    B = random.randint(-5, 5)
                C = random.randint(-10, 10)

                # Tọa độ điểm M(xm, ym)
                xm = random.randint(-5, 5)
                ym = random.randint(-5, 5)

                # Kiểm tra để đảm bảo M không thuộc Delta (để d song song chứ không trùng)
                while A * xm + B * ym + C == 0:
                    xm = random.randint(-5, 5)
                    ym = random.randint(-5, 5)

                # Đường thẳng d song song với Delta nên có dạng: Ax + By + c = 0 (c != C)
                # Vì d đi qua M: A*xm + B*ym + c = 0 => c = -(A*xm + B*ym)
                c_val = -(A * xm + B * ym)

                # So sánh d: 2x + By + c = 0 với d: 2x + by + c = 0
                # Ta có b = B và c = c_val
                b_val = B

                # Tính giá trị biểu thức T = 2b + c
                T = 2 * b_val + c_val

                # Đáp án đúng
                kq = T
                da = '$%s$' % (latex(kq))

                # Tạo các đáp án nhiễu (sai)
                s = set()
                while len(s) < 3:
                    sai = kq + random.choice([-2, -1, 1, 2, 3, 5, -3])
                    if sai != kq:
                        s.add('$%s$' % (latex(sai)))

                list_s = list(s)
                das1 = list_s[0]
                das2 = list_s[1]
                das3 = list_s[2]

                # Nội dung câu hỏi
                # d: 2x + by + c = 0
                # Delta: Ax + By + C = 0 (với A=2)
                dau_B = '+' if B > 0 else '-'
                val_B = abs(B) if abs(B) != 1 else ''
                phi_Delta = '2x %s %sy %s = 0' % (dau_B, val_B, '+ ' + str(C) if C >= 0 else str(C))
                phi_Delta = phi_Delta.replace(' 1y', ' y').replace('+ -', '- ')

                noidungcauhoi = (
                    'Biết đường thẳng $d: 2x + by + c = 0$ đi qua điểm $M(%s; %s)$ và song song với đường thẳng $\\Delta: %s$. Giá trị biểu thức $T = 2b + c$ bằng bao nhiêu?'
                    % (latex(xm), latex(ym), phi_Delta)
                )

                # Các đáp án
                da_d = '\\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                # Xử lý hiển thị dấu cho lời giải
                B_latex = latex(B)
                c_latex = latex(c_val)

                loigiai = (
                    'Vì $d // \\Delta$ nên đường thẳng $d$ có dạng: $2x %s %sy + c = 0$ với $c \\neq %s$.\\\\'
                    'Vì $d$ đi qua điểm $M(%s; %s)$ nên thay tọa độ $M$ vào phương trình $d$ ta được:\\\\'
                    '$2 \\cdot (%s) %s %s \\cdot (%s) + c = 0 \\Rightarrow %s + c = 0 \\Rightarrow c = %s$.\\\\'
                    'Khi đó phương trình đường thẳng $d$ là: $2x %s %sy %s = 0$.\\\\'
                    'So sánh với dạng $2x + by + c = 0$, ta suy ra $b = %s$ và $c = %s$.\\\\'
                    'Vậy $T = 2b + c = 2 \\cdot (%s) + (%s) = %s$.'
                    % (dau_B, val_B, latex(C), latex(xm), latex(ym),
                       latex(xm), dau_B, val_B if val_B != '' else '1', latex(ym), latex(A*xm + B*ym), latex(c_val),
                       dau_B, val_B, '+ ' + str(c_val) if c_val >= 0 else str(c_val),
                       latex(b_val), latex(c_val), latex(b_val), latex(c_val), latex(kq))
                )
                # Dọn dẹp dấu trong lời giải
                loigiai = loigiai.replace('+ -', '- ').replace(' 1y', ' y')
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

