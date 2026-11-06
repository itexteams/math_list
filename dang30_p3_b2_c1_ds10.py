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


def bt_dang30_p3_b2_c1_ds10(self):
            # Khai báo các tham số
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khởi tạo ngẫu nhiên số lượng học sinh ở các phần giao nhau của biểu đồ Venn
                x3 = randint(3, 6)           # Số học sinh giỏi cả 3 môn
                only_TL = randint(5, 12)     # Chỉ giỏi Toán và Lý
                only_TV = randint(5, 12)     # Chỉ giỏi Toán và Văn
                only_LV = randint(5, 12)     # Chỉ giỏi Lý và Văn

                only_T = randint(15, 30)     # Chỉ giỏi Toán
                only_L = randint(15, 30)     # Chỉ giỏi Lý

                only_V = randint(15, 30)     # Chỉ giỏi Văn

                # Tính toán ngược lại các số liệu đề bài cho phù hợp thực tế
                T = only_T + only_TL + only_TV + x3
                L = only_L + only_TL + only_LV + x3
                V = only_V + only_TV + only_LV + x3

                T_cap_L = only_TL + x3
                T_cap_V = only_TV + x3
                L_cap_V = only_LV + x3

                T_cup_L = T + L - T_cap_L
                T_cup_V = T + V - T_cap_V
                L_cup_V = L + V - L_cap_V

                # Đáp án đúng: tổng số học sinh chỉ xuất sắc đúng 1 môn
                kq = only_T + only_L + only_V

                # Các đáp án trắc nghiệm
                da = '$%s$' % latex(kq)

                # Tạo ngẫu nhiên các phương án sai không trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    val = kq + randint(-15, 15)
                    if val != kq and val > 0:
                        s.add('$%s$' % latex(val))
                s = list(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Trong Kỳ thi tốt nghiệp phổ thông, ở một trường kết quả số thí sinh đạt danh hiệu xuất sắc như sau: Về môn Toán: $%s$ thí sinh; Về môn Vật lý: $%s$ thí sinh; Về môn Văn: $%s$ thí sinh; Về môn Toán hoặc môn Vật lý: $%s$ thí sinh; Về môn Toán hoặc môn Văn: $%s$ thí sinh; Về môn Vật lý hoặc môn Văn: $%s$ thí sinh; Về cả $3$ môn: $%s$ thí sinh. Số học sinh nhận được danh hiệu xuất sắc về một môn bằng bao nhiêu?'''
                                 %(latex(T), latex(L), latex(V), latex(T_cup_L), latex(T_cup_V), latex(L_cup_V), latex(x3)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $T$, $L$, $V$ lần lượt là tập hợp các thí sinh đạt danh hiệu xuất sắc về môn Toán, Vật lý và Văn. \\\\
            Số học sinh xuất sắc cả hai môn Toán và Vật lý là: \\\\
            $|T \\cap L| = |T| + |L| - |T \\cup L| = %s + %s - %s = %s$ (thí sinh). \\\\
            Số học sinh xuất sắc cả hai môn Toán và Văn là: \\\\
            $|T \\cap V| = |T| + |V| - |T \\cup V| = %s + %s - %s = %s$ (thí sinh). \\\\
            Số học sinh xuất sắc cả hai môn Vật lý và Văn là: \\\\
            $|L \\cap V| = |L| + |V| - |L \\cup V| = %s + %s - %s = %s$ (thí sinh). \\\\
            Số học sinh chỉ xuất sắc đúng một môn Toán là: \\\\
            $|T| - |T \\cap L| - |T \\cap V| + |T \\cap L \\cap V| = %s - %s - %s + %s = %s$ (thí sinh). \\\\
            Số học sinh chỉ xuất sắc đúng một môn Vật lý là: \\\\
            $|L| - |T \\cap L| - |L \\cap V| + |T \\cap L \\cap V| = %s - %s - %s + %s = %s$ (thí sinh). \\\\
            Số học sinh chỉ xuất sắc đúng một môn Văn là: \\\\
            $|V| - |T \\cap V| - |L \\cap V| + |T \\cap L \\cap V| = %s - %s - %s + %s = %s$ (thí sinh). \\\\
            Vậy số học sinh nhận được danh hiệu xuất sắc về đúng một môn là: \\\\
            $%s + %s + %s = %s$ (thí sinh).'''
                           %(latex(T), latex(L), latex(T_cup_L), latex(T_cap_L),
                             latex(T), latex(V), latex(T_cup_V), latex(T_cap_V),
                             latex(L), latex(V), latex(L_cup_V), latex(L_cap_V),
                             latex(T), latex(T_cap_L), latex(T_cap_V), latex(x3), latex(only_T),
                             latex(L), latex(T_cap_L), latex(L_cap_V), latex(x3), latex(only_L),
                             latex(V), latex(T_cap_V), latex(L_cap_V), latex(x3), latex(only_V),
                             latex(only_T), latex(only_L), latex(only_V), latex(kq)))

                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

