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


def bt_dang10_p1_b1_c6_ds11(self):
            # Khai báo biến
            # Khai báo các biến và hằng số ngẫu nhiên
            # N: Tổng số tấm thẻ (ngẫu nhiên từ 12 đến 20)
            N = randint(14, 20)

            # Tập hợp các số lẻ từ 1 đến N (Biến cố A)
            tap_A = [i for i in range(1, N + 1) if i % 2 != 0]
            str_tap_A = "{" + ", ".join(map(str, tap_A)) + "}"

            # Phương án đúng (Biến cố xung khắc): Chọn một số chẵn k sao cho tập các số chia hết cho k toàn số chẵn
            # Thông thường chọn chia hết cho 4, 6, 8, 10... vì chúng chắc chắn không chứa số lẻ
            k_dung = random.choice([4, 6, 8])
            tap_dung = [i for i in range(1, N + 1) if i % k_dung == 0]
            str_tap_dung = ", ".join(map(str, tap_dung))

            # Các phương án sai (Không xung khắc với A - tức là có chứa ít nhất 1 số lẻ)
            # Phương án sai 1: Số nhỏ hơn m (m > 1) -> luôn chứa số 1
            m = randint(5, 9)
            tap_s1 = [i for i in range(1, m)]
            str_tap_s1 = ", ".join(map(str, tap_s1))

            # Phương án sai 2: Chia hết cho 3 (luôn chứa số 3)
            tap_s2 = [i for i in range(1, N + 1) if i % 3 == 0]
            str_tap_s2 = ", ".join(map(str, tap_s2))

            # Phương án sai 3: Chia hết cho 5 (luôn chứa số 5)
            tap_s3 = [i for i in range(1, N + 1) if i % 5 == 0]
            str_tap_s3 = ", ".join(map(str, tap_s3))

            # Câu hỏi
            noidungcauhoi = ('''Một hộp chứa $%s$ tấm thẻ cùng loại được đánh số từ $1$ đến $%s$. Chọn ra ngẫu nhiên $1$ thẻ từ hộp. Gọi $A$ là biến cố "Số ghi trên thẻ được chọn là số lẻ", biến cố nào sau đây là biến cố xung khắc với biến cố $A$?'''
                             % (latex(N), latex(N)))

            # Các đáp án
            da_d = ('\\True Số ghi trên thẻ được chọn chia hết cho %s' % (latex(k_dung)))
            da_s1 = ('Số ghi trên thẻ được chọn nhỏ hơn %s' % (latex(m)))
            da_s2 = ('Số ghi trên thẻ được chọn chia hết cho $3$')
            da_s3 = ('Số ghi trên thẻ được chọn chia hết cho $5$')

            # Đưa các đáp án vào danh sách và xáo trộn
            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # Nội dung lời giải chi tiết
            loigiai = ('''Ta có $A = %s$. \\\\
                         Xét các phương án: \\\\
                         - Số ghi trên thẻ được chọn nhỏ hơn $%s$: $%s$. Tập hợp này chứa các số lẻ (ví dụ như $1, 3...$) nên không xung khắc với $A$. \\\\
                         - Số ghi trên thẻ được chọn chia hết cho $3$: $%s$. Tập hợp này chứa các số lẻ (ví dụ như $3, 9...$) nên không xung khắc với $A$. \\\\
                         - Số ghi trên thẻ được chọn chia hết cho $5$: $%s$. Tập hợp này chứa các số lẻ (ví dụ như $5, 15...$) nên không xung khắc với $A$. \\\\
                         - Số ghi trên thẻ được chọn chia hết cho $%s$: $%s$. Vì tập hợp này chỉ bao gồm các số chẵn, nên không có phần tử nào chung với tập hợp các số lẻ $A$. \\\\
                         Do đó biến cố xung khắc với biến cố $A$ là "Số ghi trên thẻ được chọn chia hết cho $%s$".'''
                       % (str_tap_A, latex(m), str_tap_s1, str_tap_s2, str_tap_s3, latex(k_dung), str_tap_dung, latex(k_dung)))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_ans[0]) + '}\n'
                       '{' + str(list_ans[1]) + '}\n'
                       '{' + str(list_ans[2]) + '}\n'
                       '{' + str(list_ans[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

