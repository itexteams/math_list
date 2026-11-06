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


def bt_dang45_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến và danh sách tên để random
            list_names_all = ["An", "Bình", "Chi", "Dũng", "Huệ", "Hồng", "Lan", "Mai", "Nam", "Phúc"]

            # Chọn ngẫu nhiên số lượng bạn từ 5 đến 8 để bài toán đa dạng
            n = randint(5, 8)
            selected_names = list_names_all[:n]
            names_str = ", ".join(selected_names[:-1]) + " và " + selected_names[-1]

            # Tính toán các giá trị
            # Không gian mẫu: n!
            n_factorial = math.factorial(n)

            # Số cách xếp An và Bình cạnh nhau:
            # Coi An và Bình là 1 nhóm (X): có 2! = 2 cách xếp An-Bình hoặc Bình-An
            # Xếp nhóm (X) và (n-2) bạn còn lại: có (n-1)! cách
            favorable_ways = 2 * math.factorial(n - 1)

            # Xác suất P = (2 * (n-1)!) / n! = 2 / n
            prob = Rational(2, n)

            # Tạo các đáp án sai
            wrong_answers = set()
            while len(wrong_answers) < 3:
                # Tạo các phân số khác 2/n
                den = randint(n - 2, n + 5)
                num = randint(1, 5)
                w_prob = Rational(num, den)
                if w_prob != prob and w_prob < 1:
                    wrong_answers.add("$%s$" % latex(w_prob))

            list_wrong = list(wrong_answers)

            # Đáp án đúng
            da_dung = "$%s$" % latex(prob)

            # Câu hỏi
            noidungcauhoi = ("Xếp ngẫu nhiên %s bạn %s vào một dãy ghế có %s chỗ ngồi. Xác suất để %s và %s luôn ngồi cạnh nhau bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm)."
                             % (latex(n), names_str, latex(n), selected_names[0], selected_names[1]))

            # Các đáp án cho vào danh sách
            da_d = "\\True " + str(da_dung)
            da_s1 = str(list_wrong[0])
            da_s2 = str(list_wrong[1])
            da_s3 = str(list_wrong[2])

            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            h1=prob
            number = Decimal(float(h1))  # Số cần làm tròn
            kq1 = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            kqz=str(kq1).replace('.', ',')

            # Nội dung lời giải chi tiết theo yêu cầu
            loigiai = ("Số cách xếp %s bạn vào dãy ghế gồm %s chỗ là một hoán vị của %s phần tử nên có $n(\\Omega) = %s! = %s$ cách. \\\\ "
                       "Gọi biến cố A: \"An và Bình luôn ngồi cạnh nhau\". \\\\ "
                       "Buộc An và Bình thành một nhóm, có $2! = 2$ cách sắp xếp nội bộ hai bạn này. \\\\ "
                       "Coi nhóm này là một phần tử mới kết hợp với %s bạn còn lại, ta có %s phần tử. \\\\ "
                       "Số cách xếp các phần tử này là $%s!$ cách. \\\\ "
                       "Số kết quả thuận lợi cho biến cố A là $n(A) = 2 \\cdot %s! = %s$ cách. \\\\ "
                       "Vậy xác suất để An và Bình luôn ngồi cạnh nhau là $P(A) = \\frac{n(A)}{n(\\Omega)} = \\frac{2 \\cdot %s!}{%s!} = \\frac{2}{%s} = %s \\approx %s$."
                       % (latex(n), latex(n), latex(n), latex(n), latex(n_factorial), 
                          latex(n-2), latex(n-1), latex(n-1), 
                          latex(n-1), latex(favorable_ways),
                          latex(n-1), latex(n), latex(n), latex(prob), kqz))
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(kqz))
            # Xuất câu trắc nghiệm (Không dùng raw string r'' theo yêu cầu)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

