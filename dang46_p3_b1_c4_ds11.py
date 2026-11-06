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


def bt_dang46_p3_b1_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các thông số cho bài toán
                p = random.choice([50, 60, 75, 80, 90]) # Phần trăm nước được xử lí
                u1 = random.randint(5, 50) * 10         # Lượng nước ban đầu (m^3)

                q_val = p / 100
                # Chuyển đổi định dạng số thập phân sử dụng dấu phẩy
                q_str = str(q_val).replace('.', ',')

                # Tính tổng S theo công thức cấp số nhân lùi vô hạn S = u1 / (1 - q)
                S_val = (u1 * 100) / (100 - p)
                if S_val.is_integer():
                    S = int(S_val)
                else:
                    S = round(S_val, 1)
                S_str = str(S).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (S_str)]
                da = random.choice(du)

                # Tạo danh sách các phương án sai (đảm bảo giá trị > 0)
                s_list = [
                    int(S_val) + u1,
                    int(S_val) - u1 if int(S_val) - u1 > 0 else int(S_val) + 50,
                    int(S_val) * 2,
                    int(S_val / 2) if int(S_val / 2) > 0 else int(S_val) + 120,
                    int(S_val) + 100,
                    int(S_val) - 100 if int(S_val) - 100 > 0 else int(S_val) + 150,
                    int(S_val) + 200
                ]

                # Lọc loại bỏ trùng lặp với đáp án đúng và giữa các đáp án sai với nhau
                s_unique = list(set([x for x in s_list if x != S]))
                random.shuffle(s_unique)

                das1 = '$%s$' % str(s_unique[0]).replace('.', ',')
                das2 = '$%s$' % str(s_unique[1]).replace('.', ',')
                das3 = '$%s$' % str(s_unique[2]).replace('.', ',')

                # Câu hỏi (Lưu ý: Không dùng prefix r, các ký tự escape \\ đều được xử lý đúng chuẩn)
                noidungcauhoi = ('''Tại một nhà máy, người ta đo được rằng $%s\\%%$ lượng nước sau khi qua sử dụng được xử lí và tái sử dụng. Với $%s$ $\\mathrm{m}^3$ ban đầu được sử dụng tại nhà máy, khi quá trình xử lí và tái sử dụng lặp lại mãi mãi thì nhà máy sử dụng được tổng lượng nước là bao nhiêu?'''
                                 % (p, u1))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $u_n$ là lượng nước nhà máy sử dụng lần thứ $n$.\\\\
            Khi đó lượng nước nhà máy sử dụng lần lượt là\\\\
            $u_1 = %s ; u_2 = %s \\cdot %s ; u_3 = %s \\cdot (%s)^2$\\\\
            $\\dots$\\\\
            Đặt $S$ là tổng lượng nước nhà máy sử dụng, ta có\\\\
            $S = u_1 + u_2 + u_3 + \\dots = %s + %s \\cdot %s + %s \\cdot (%s)^2 + \\dots$\\\\
            Như vậy tổng lượng nước nhà máy sử dụng là một cấp số nhân lùi vô hạn với $u_1 = %s$ và $q = %s$\\\\
            Suy ra $S = \\frac{%s}{1 - %s} = %s$ ($\\mathrm{m}^3$)\\\\
            Vậy, với $%s$ $\\mathrm{m}^3$ ban đầu được sử dụng tại nhà máy, khi quá trình xử lí và tái sử dụng lặp lại mãi mãi, nhà máy sử dụng được tổng lượng nước là $%s$ $\\mathrm{m}^3$.'''
                           % (u1, u1, q_str, u1, q_str,
                              u1, u1, q_str, u1, q_str,
                              u1, q_str,
                              u1, q_str, S_str,
                              u1, S_str))
                dapan='\\shortans[0]{$%s$}\n'%(S_str)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

