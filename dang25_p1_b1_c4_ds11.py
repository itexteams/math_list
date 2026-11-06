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


def bt_dang25_p1_b1_c4_ds11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # 1. Random nghiệm a (nghiệm đúng)
                # Chọn nghiệm nguyên nhỏ để bài toán đẹp (từ 1 đến 5 hoặc -5 đến -1)
                nghiem_a = randint(1, 5) 


                val_B = 1 - 2 * nghiem_a
                val_C = nghiem_a**2

                # Xử lý hiển thị dấu cho đẹp (Vế phải phương trình)
                # Tạo đa thức symbolic để in ra LaTeX đẹp tự động
                a_sym = symbols('a')
                ve_phai_expr = a_sym**2 + val_B*a_sym + val_C
                str_ve_phai = latex(ve_phai_expr)

                # 3. Các đáp án trắc nghiệm
                # Đáp án đúng
                kq = nghiem_a

                # Tạo đáp án nhiễu
                set_answers = set()
                set_answers.add(kq)
                while len(set_answers) < 4:
                    # Tạo nhiễu bằng cách cộng trừ 1, 2 hoặc đổi dấu
                    fake = random.choice([kq + randint(1,3), kq - randint(1,3), -kq])
                    set_answers.add(fake)

                list_ans = list(set_answers)
                # Đảm bảo vị trí đáp án đúng ngẫu nhiên sau này, 
                # nhưng ở bước này ta cần lấy ra để gán vào biến da, das1...
                # Tuy nhiên code mẫu của bạn dùng logic remove, nên ta làm theo:

                da = '$a = %s$' % latex(kq) # Đáp án đúng

                # Xóa đáp án đúng khỏi list để lấy đáp án sai
                list_ans.remove(kq)

                das1 = '$a = %s$' % latex(list_ans[0])
                das2 = '$a = %s$' % latex(list_ans[1])
                das3 = '$a = %s$' % latex(list_ans[2])

                # 4. Nội dung câu hỏi
                # Tử số: an^2 + a^2n + 1 (giữ nguyên cấu trúc đề gốc cho giống)
                # Mẫu số: (n+1)^2
                noidungcauhoi = ('''Cho $a \\in \\mathbb{R}$ sao cho giới hạn $\\displaystyle \\lim_{n \\to +\\infty} \\frac{an^2 + a^2n + 1}{(n+1)^2} = %s$. Khi đó khẳng định nào sau đây là đúng?'''
                                 % (str_ve_phai))

                # 5. Các đáp án để shuffle
                da_d = '\\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # 6. Nội dung lời giải
                # Tạo phương trình hiển thị bước giải: a^2 - 2*nghiem_a*a + nghiem_a^2 = 0
                # Bước chuyển vế: a^2 + (val_B)*a + val_C = a

                # Logic hiển thị phương trình bậc 2 cuối cùng: (a - nghiem_a)^2 = 0
                pt_cuoi = a_sym**2 - 2*nghiem_a*a_sym + nghiem_a**2

                loigiai = ('''Ta có $\\displaystyle \\lim_{n \\to +\\infty} \\frac{an^2 + a^2n + 1}{(n+1)^2} = \\lim_{n \\to +\\infty} \\frac{an^2 + a^2n + 1}{n^2 + 2n + 1} = \\lim_{n \\to +\\infty} \\frac{a + \\frac{a^2}{n} + \\frac{1}{n^2}}{1 + \\frac{2}{n} + \\frac{1}{n^2}} = a$. \\\\
                Theo giả thiết ta có:
                $$%s = a \\Leftrightarrow %s = 0 \\Leftrightarrow (a - %s)^2 = 0 \\Leftrightarrow a = %s.$$'''
                % (str_ve_phai, latex(pt_cuoi), latex(nghiem_a), latex(nghiem_a)))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

