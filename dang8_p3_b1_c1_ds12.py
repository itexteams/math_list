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


def bt_dang8_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random thời điểm đạt độ cao cực đại (để đảm bảo số đẹp)
                # Chọn t_max từ danh sách các giá trị đẹp để v0 = t_max * 9.8 có dạng gọn
                t_values = [2, 2.5, 3, 3.5, 4, 4.5, 5]
                t_max = random.choice(t_values)

                # Độ cao ban đầu h0 (mét)
                h0 = randint(1, 10)

                # Vận tốc ban đầu v0 (m/s)
                v0 = round(9.8 * t_max, 1)

                # Đáp án đúng
                kq_num = t_max
                kq = str(kq_num).replace('.', ',')

                # Các đáp án trắc nghiệm sai lệch quanh đáp án đúng
                du = ['$%s$ giây'%(kq)]
                da = random.choice(du)

                # Tạo các phương án nhiễu (sai lệch 0.5, 1, 1.5, 2 giây...)
                s_vals = [
                    t_max + 0.5, t_max + 1, t_max + 1.5, t_max + 2,
                    t_max - 0.5, t_max - 1, t_max - 1.5
                ]
                # Lọc bỏ các giá trị <= 0
                s_vals = [v for v in s_vals if v > 0]

                s = []
                for val in s_vals:
                    val_str = str(round(val, 1)).replace('.', ',')
                    s.append('$%s$ giây'%(val_str))

                s = list(set(s)) # Loại bỏ trùng lặp nếu có

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Chuẩn hóa hiển thị số thập phân cho đề bài và lời giải
                v0_str = str(v0).replace('.', ',')
                h0_str = str(h0)

                # Câu hỏi
                noidungcauhoi = ('''Một vật được phóng thẳng đứng lên trên từ độ cao $%s$ m với vận tốc ban đầu là $%s$ m/s. Trong Vật lí, ta biết rằng khi bỏ qua sức cản của không khí thì độ cao $h$ (mét) của vật sau $t$ (giây) được cho bởi công thức
                                 $$h(t) = %s + %s t - 4,9 t^2.$$
                                 Hỏi tại thời điểm nào thì vật đạt độ cao lớn nhất?'''
                                 %(latex(h0), latex(v0_str), latex(h0), latex(v0_str)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Hàm số biểu diễn độ cao của vật theo thời gian là một hàm số bậc hai:
                           $$h(t) = -4,9 t^2 + %s t + %s.$$
                           Vì hệ số của $t^2$ là $a = -4,9 < 0$ nên đồ thị hàm số là một parabol quay bề lõm xuống dưới. \\\\
                           Do đó, hàm số đạt giá trị lớn nhất tại đỉnh của parabol, tức là tại thời điểm:
                           $$t = -\\frac{b}{2a} = -\\frac{%s}{2 \\cdot (-4,9)} = %s \\text{ (giây)}.$$
                           Vậy tại thời điểm $%s$ giây thì vật đạt độ cao lớn nhất.'''
                           %(latex(v0_str), latex(h0_str), latex(v0_str), latex(kq), latex(kq)))

                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

