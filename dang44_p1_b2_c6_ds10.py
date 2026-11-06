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


def bt_dang44_p1_b2_c6_ds10(self):
            #Khai báo biến
            # Ở bài gốc là 24, ta có thể cho chạy từ 20 đến 30
            n_students = random.randint(20, 30)
            k_exams = 4 # Số lần thi
            m_repeat = 2 # Số lần ngồi cùng một vị trí

            # Tính toán các giá trị
            # n(Omega) = n^4
            omega = n_students**k_exams

            # n(A) = C(4,2) * n * (n-1) * (n-2)

            comb_4_2 = math.comb(k_exams, m_repeat)
            n_A = comb_4_2 * n_students * (n_students - 1) * (n_students - 2)

            # Tính xác suất rút gọn
            p_A = frac(n_A, omega)
            tu_dung = p_A.numerator
            mau_dung = p_A.denominator

            # B4: Tạo các phương án sai không trùng với đáp án đúng
            wrong_answers = set()
            while len(wrong_answers) < 3:
                # Tạo các phương án sai bằng cách thay đổi tử số hoặc mẫu số
                # Cách 1: Thay đổi tử số của phân số đã rút gọn
                w_tu = tu_dung + random.choice([-5, -3, 3, 5, 10])
                if w_tu > 0 and w_tu != tu_dung:
                    wrong_answers.add("$%s$" % (latex(Rational(w_tu, mau_dung))))

                # Cách 2: Logic sai (ví dụ quên nhân C_4^2 hoặc dùng C_4^3)
                n_A_wrong = math.comb(4, 3) * n_students * (n_students - 1)
                p_wrong = frac(n_A_wrong, omega)
                wrong_answers.add("$%s$" % (latex(Rational(p_wrong.numerator, p_wrong.denominator))))

            list_wrong = list(wrong_answers)[:3]

            # Đáp án đúng
            da_dung = "$%s$" % (latex(Rational(tu_dung, mau_dung)))

            # B2: Viết nội dung câu hỏi và lời giải chi tiết
            noidungcauhoi = ('''Trong kỳ thi THPT Quốc Gia, mỗi lớp gồm $%s$ thí sinh được sắp xếp vào $%s$ bàn khác nhau. Bạn Nam là một thí sinh dự thi, bạn đăng kí $%s$ môn thi và cả $%s$ lần thi đều thi tại một phòng duy nhất. Giả sử giám thị xếp thí sinh vào vị trí một cách ngẫu nhiên. Xác suất để trong $%s$ lần thi thì Nam có đúng hai lần ngồi cùng vào một vị trí là'''
                             % (latex(n_students), latex(n_students), latex(k_exams), latex(k_exams), latex(k_exams)))

            da_d = ('\\True ' + str(da_dung))
            da_s1 = str(list_wrong[0])
            da_s2 = str(list_wrong[1])
            da_s3 = str(list_wrong[2])

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Lời giải chi tiết không viết tắt
            loigiai = ('''Số phần tử của không gian mẫu là số cách sắp xếp chỗ ngồi ngẫu nhiên trong $%s$ lần thi của Nam. \\\\
                         Suy ra số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = %s^{%s} = %s$. \\\\
                         Gọi $A$ là biến cố "$%s$ lần thi thì Nam có đúng $%s$ lần ngồi vào cùng một vị trí". Ta mô tả không gian của biến cố $A$ như sau: \\\\
                         - Trong $%s$ lần thi, số cách chọn ra $%s$ lần để Nam ngồi cùng vào một vị trí là $C_{%s}^{%s} = %s$ cách. \\\\
                         - Giả sử tại hai lần đó, Nam ngồi vào cùng một vị trí: có $%s$ cách chọn vị trí ngồi. \\\\
                         - Hai lần thi còn lại, Nam phải ngồi vào các vị trí khác với vị trí ban đầu và cũng phải khác nhau (để đảm bảo có đúng $%s$ lần trùng vị trí). \\\\
                         - Số cách chọn chỗ ngồi cho lần thứ ba là $%s - 1 = %s$ cách. \\\\
                         - Số cách chọn chỗ ngồi cho lần thứ tư là $%s - 2 = %s$ cách. \\\\
                         Suy ra số phần tử của biến cố $A$ là $n\\left(A\\right) = C_{%s}^{%s} \\cdot %s \\cdot %s \\cdot %s = %s$. \\\\
                         Vậy xác suất cần tính là $P\\left(A\\right) = \\frac{n\\left(A\\right)}{n\\left(\\Omega\\right)} = \\frac{C_{%s}^{%s} \\cdot %s \\cdot %s \\cdot %s}{%s^{%s}} = %s$.'''
                       % (latex(k_exams), latex(n_students), latex(k_exams), latex(omega),
                          latex(k_exams), latex(m_repeat),
                          latex(k_exams), latex(m_repeat), latex(k_exams), latex(m_repeat), latex(comb_4_2),
                          latex(n_students), latex(m_repeat),
                          latex(n_students), latex(n_students - 1),
                          latex(n_students), latex(n_students - 2),
                          latex(k_exams), latex(m_repeat), latex(n_students), latex(n_students - 1), latex(n_students - 2), latex(n_A),
                          latex(k_exams), latex(m_repeat), latex(n_students), latex(n_students - 1), latex(n_students - 2), latex(n_students), latex(k_exams), latex(Rational(tu_dung, mau_dung))))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\n\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

