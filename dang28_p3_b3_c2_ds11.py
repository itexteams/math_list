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


def bt_dang28_p3_b3_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random cạnh hình vuông ban đầu a1 và số hình vuông k
                a1 = random.randint(3, 10)
                k = random.randint(4, 7)

                # Tính diện tích hình vuông ban đầu S1 và tổng T
                S1 = a1**2
                T_num = S1 * (2**k - 1)
                T_den = 2 ** (k - 1)

                # Chuyển T về dạng số thập phân sử dụng dấu phẩy
                T_decimal = Decimal(T_num) / Decimal(T_den)
                T_str = str(T_decimal).replace('.', ',')

                # Đáp án đúng
                da = '$%s$' % (k)

                # Tạo các phương án sai không trùng nhau và không trùng đáp án đúng
                s_set = set()
                while len(s_set) < 6:
                    diff = random.choice([-3, -2, -1, 1, 2, 3, 4])
                    k_wrong = k + diff
                    if k_wrong > 0 and k_wrong != k:
                        s_set.add('$%s$' % (k_wrong))

                s = list(s_set)
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Nội dung câu hỏi
                noidungcauhoi = (
                    '''Cho hình vuông $A_1B_1C_1D_1$ có cạnh bằng $%sm$. Ta lấy trung điểm các cạnh hình vuông $A_1B_1C_1D_1$ để tạo thành hình vuông mới $A_2B_2C_2D_2$. Từ hình vuông $A_2B_2C_2D_2$ lại làm như trên ta được các dãy hình vuông $A_3B_3C_3D_3, \\dots, A_kB_kC_kD_k$. Gọi $S_i$ là diện tích của hình vuông $A_iB_iC_iD_i, i \\in \\{1; 2; 3; \\dots; k\\}$. Đặt $T = S_1 + S_2 + \\dots + S_k$. Biết $T = %s$. Giá trị của $k$ bằng bao nhiêu?'''
                    % (latex(a1), T_str)
                )

                # Các đáp án
                da_d = '\\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (
                    '''Gọi độ dài cạnh hình vuông $A_1B_1C_1D_1$ là $a_1$, diện tích hình vuông $A_1B_1C_1D_1$ là $S_1 = a_1^2 = %s$, khi đó cạnh của hình vuông $A_2B_2C_2D_2$ là $a_2 = \\frac{\\sqrt{2}}{2} a_1$ nên diện tích hình vuông $A_2B_2C_2D_2$ là: $S_2 = \\left(\\frac{\\sqrt{2}}{2} a_1\\right)^2 = \\frac{1}{2} a_1^2 = \\frac{1}{2} S_1$.\\\\
            Cạnh của hình vuông $A_3B_3C_3D_3$ là: $a_3 = \\frac{\\sqrt{2}}{2} a_2$ nên diện tích hình vuông $A_3B_3C_3D_3$ là: $S_3 = \\left(\\frac{\\sqrt{2}}{2} a_2\\right)^2 = \\frac{1}{2} a_2^2 = \\frac{1}{2} S_2$.\\\\
            Tương tự ta có các $S_1, S_2, \\dots, S_k$ tạo thành một cấp số nhân có $u_1 = S_1 = %s$ và công bội $q = \\frac{1}{2}$.\\\\
            Khi đó ta có:
            $T = \\frac{u_1(q^k - 1)}{q - 1} = \\frac{%s \\cdot \\left(\\left(\\frac{1}{2}\\right)^k - 1\\right)}{\\frac{1}{2} - 1} = %s \\Leftrightarrow k = %s$.'''
                    % (latex(S1), latex(S1), latex(S1), T_str, latex(k))
                )
            dapan='\\shortans[0]{$%s$}\n'%(latex(k))
            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

