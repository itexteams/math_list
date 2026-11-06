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


def bt_dang42_p1_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random số lượng đường thẳng song song và vuông góc
                m = randint(4, 7)
                n = randint(4, 8)
                while m == n:
                    n = randint(4, 8)

                # Tính toán số tổ hợp chọn 2 trong m và 2 trong n
                res_m = binomial(m, 2)
                res_n = binomial(n, 2)
                kq_val = res_m * res_n

                # Đáp án đúng
                da = '$%s$' % (latex(kq_val))

                # Tạo các phương án sai
                s_wrong = set()
                while len(s_wrong) < 3:
                    w1 = m * n
                    w2 = binomial(m, 2) + binomial(n, 2)
                    w3 = binomial(m + 1, 2) * binomial(n, 2)
                    w4 = binomial(m, 2) * binomial(n + 1, 2)
                    w5 = kq_val + randint(5, 25)
                    w6 = kq_val - randint(5, 25)
                    # Lấy ngẫu nhiên một giá trị sai từ các công thức trên
                    val = random.choice([w1, w2, w3, w4, w5, w6])
                    if val != kq_val and val > 0:
                        s_wrong.add('$%s$' % (latex(val)))

                list_wrong = list(s_wrong)
                das1 = list_wrong[0]
                das2 = list_wrong[1]
                das3 = list_wrong[2]

                # Câu hỏi
                noidungcauhoi = ('''Trong mặt phẳng có bao nhiêu hình chữ nhật được tạo thành từ $%s$ đường thẳng phân biệt song song với nhau và $%s$ đường thẳng phân biệt vuông góc với $%s$ đường thẳng song song đó?'''
                                 % (latex(m), latex(n), latex(m)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Cứ $2$ đường thẳng song song với $2$ đường thẳng vuông góc với chúng cắt nhau tại bốn điểm là $4$ đỉnh của hình chữ nhật. \\\\
                             Số cách chọn $2$ đường thẳng trong $%s$ đường thẳng song song là $C_{%s}^{2} = %s$. \\\\
                             Số cách chọn $2$ đường thẳng trong $%s$ đường thẳng vuông góc là $C_{%s}^{2} = %s$. \\\\
                             Vậy lấy $2$ đường thẳng trong $%s$ đường thẳng song song và lấy $2$ đường thẳng trong $%s$ đường thẳng vuông góc với $%s$ đường thẳng đó ta được số hình chữ nhật là $C_{%s}^{2} \\cdot C_{%s}^{2} = %s \\cdot %s = %s$.'''
                           % (latex(m), latex(m), latex(res_m), 
                             latex(n), latex(n), latex(res_n), 
                             latex(m), latex(n), latex(m), 
                             latex(m), latex(n), latex(res_m), latex(res_n), latex(kq_val)))

            # Xuất nội dung theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\choice \n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '{' + str(list_1[0]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

