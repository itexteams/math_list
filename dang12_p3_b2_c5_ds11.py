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


def bt_dang12_p3_b2_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Thiết lập u = log2|x| và v = log2|y|
                # Để A và B là số nguyên trong phương trình:
                # (1/3)u + v = A
                # u + (1/3)v = B
                # Ta chọn u, v là bội số của 3.

                # Random u và v để bài toán có nghiệm đẹp
                list_uv = [(6, 3), (9, 3), (9, 6), (12, 6), (12, 9)]
                u, v = random.choice(list_uv)

                # Tính toán các hằng số A và B cho đề bài
                # log8|x| + log4(y^2) = 1/3*log2|x| + log2|y| = u/3 + v
                A = int(u/3 + v)
                # log8|y| + log4(x^2) = 1/3*log2|y| + log2|x| = v/3 + u
                B = int(v/3 + u)

                # Tính toán các giá trị trung gian cho lời giải
                tong_AB = A + B
                hieu_BA = B - A

                log2_xy = int(3 * tong_AB / 4)
                val_xy = 2**log2_xy

                log2_x_chia_y = int(3 * hieu_BA / 2)
                val_x_chia_y = 2**log2_x_chia_y

                abs_x = 2**u
                abs_y = 2**v

                # Kết quả cuối cùng P = |x| - |y|
                kq_val = abs_x - abs_y
                kq = str(kq_val)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % kq]
                da = du[0]

                # Tạo các phương án sai (không trùng với đáp án đúng)
                s = set()
                while len(s) < 3:
                    sai = random.choice([
                        abs_x + abs_y, 
                        abs_y - abs_x, 
                        abs_x, 
                        abs_y, 
                        int(abs_x/2), 
                        abs_y * 2,
                        kq_val + random.randint(2, 10),
                        kq_val - random.randint(2, 10)
                    ])
                    if sai != kq_val and sai > 0:
                        s.add('$%s$' % str(sai))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                noidungcauhoi = (r'''Cho $\log_{8} |x| + \log_{4} y^2 = %s$ và $\log_{8} |y| + \log_{4} x^2 = %s$. Giá trị của biểu thức $P = |x| - |y|$ bằng bao nhiêu?'''
                                 % (latex(A), latex(B)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_ans = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_ans)

                # Nội dung lời giải
                loigiai = (r'''Điều kiện: $x, y \neq 0$. \\
                            Cộng vế với vế của hai phương trình, ta được: \\
                            $\log_{8} |xy| + \log_{4} x^2 y^2 = %s \Leftrightarrow \frac{1}{3}\log_{2} |xy| + \log_{2} |xy| = %s \Leftrightarrow \log_{2} |xy| = %s \Leftrightarrow |xy| = %s \quad (1)$ \\
                            Trừ vế với vế của hai phương trình, ta được: \\
                            $\log_{8} \left| \frac{y}{x} \right| + \log_{4} \frac{x^2}{y^2} = %s \Leftrightarrow -\frac{1}{3}\log_{2} \left| \frac{x}{y} \right| + \log_{2} \left| \frac{x}{y} \right| = %s \Leftrightarrow \log_{2} \left| \frac{x}{y} \right| = %s \Leftrightarrow \left| \frac{x}{y} \right| = %s \Leftrightarrow |x| = %s |y| \quad (2)$ \\
                            Từ (1) và (2) suy ra $|y| = %s \Rightarrow |x| = %s \Leftrightarrow P = %s$.'''
                           % (latex(tong_AB), latex(tong_AB), latex(log2_xy), latex(val_xy),
                              latex(hieu_BA), latex(hieu_BA), latex(log2_x_chia_y), latex(val_x_chia_y), latex(val_x_chia_y),
                              latex(abs_y), latex(abs_x), latex(kq)))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

