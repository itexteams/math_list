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


def bt_dang16_p1_b3_c6_ds11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Random xác suất của 2 cảm biến (từ 0.70 đến 0.95)
        pa_val = random.choice([75, 80, 85, 90, 92, 95])
        pb_val = random.choice([75, 80, 85, 90, 92, 95])

        # Dùng Decimal để tính toán chính xác
        pA = Decimal(str(pa_val)) / Decimal('100')
        pB = Decimal(str(pb_val)) / Decimal('100')

        # Tính xác suất đối
        pA_bar = Decimal('1') - pA
        pB_bar = Decimal('1') - pB

        # Tính đáp án đúng (ít nhất 1 cảm biến phát tín hiệu)
        ans = Decimal('1') - pA_bar * pB_bar

        # Chuỗi định dạng hiển thị dấu phẩy
        str_pA = str(pA).replace('.', ',')
        str_pB = str(pB).replace('.', ',')
        str_pA_bar = str(pA_bar).replace('.', ',')
        str_pB_bar = str(pB_bar).replace('.', ',')
        str_ans = str(ans).replace('.', ',')

        # Đáp án đúng
        da = '$%s$' % str_ans

        # Tạo danh sách các phương án sai
        s_set = set()
        # Sai lầm 1: P(A) * P(B)
        s_set.add(str(pA * pB).replace('.', ','))
        # Sai lầm 2: 1 - P(A) * P(B)
        s_set.add(str(Decimal('1') - pA * pB).replace('.', ','))

        # Sinh thêm các phương án ngẫu nhiên nếu trùng
        while len(s_set) < 5:
            delta = Decimal(str(random.choice([-3, -2, -1, 1, 2, 3]))) * Decimal('0.01')
            fake_ans = ans + delta
            if Decimal('0') < fake_ans < Decimal('1'):
                s_set.add(str(fake_ans).replace('.', ','))

        s_set.discard(str_ans) # Đảm bảo không trùng đáp án đúng
        s_list = list(s_set)[:3]

        das1 = '$%s$' % s_list[0]
        das2 = '$%s$' % s_list[1]
        das3 = '$%s$' % s_list[2]

        # Câu hỏi
        noidungcauhoi = ('''Một hệ thống cảnh báo cháy tự động của một tòa nhà được lắp đặt hai cảm biến $A$ và $B$ hoạt động độc lập với nhau. Khi xảy ra sự cố cháy, xác suất để cảm biến $A$ và cảm biến $B$ phát tín hiệu cảnh báo tương ứng là $%s$ và $%s$. Xác suất để khi xảy ra sự cố cháy, tòa nhà nhận được tín hiệu cảnh báo từ ít nhất một trong hai cảm biến là'''
                         % (str_pA, str_pB))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Gọi $X$ là biến cố: ''Cảm biến $A$ phát tín hiệu cảnh báo'', ta có $P(X) = %s \\Rightarrow P(\\overline{X}) = %s$.\\\\
    Gọi $Y$ là biến cố: ''Cảm biến $B$ phát tín hiệu cảnh báo'', ta có $P(Y) = %s \\Rightarrow P(\\overline{Y}) = %s$.\\\\
    Biến cố: ''Tòa nhà nhận được tín hiệu cảnh báo từ ít nhất một trong hai cảm biến'' là biến cố đối của biến cố ''Không có cảm biến nào phát tín hiệu'' (biến cố $\\overline{X} \\cdot \\overline{Y}$).\\\\
    Vì $X$ và $Y$ là hai biến cố độc lập nên xác suất cần tìm là:\\\\
    $P = 1 - P(\\overline{X}) \\cdot P(\\overline{Y}) = 1 - %s \\cdot %s = 1 - %s = %s$.'''
                   % (str_pA, str_pA_bar, 
                      str_pB, str_pB_bar, 
                      str_pA_bar, str_pB_bar, 
                      str(pA_bar * pB_bar).replace('.', ','), str_ans))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choice \n'
        '{'+str(list_1[0])+'}\n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

