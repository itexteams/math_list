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


def bt_dang4_p3_b1_c6_ds10(self):
            # Khai báo biến
            # B2 & B3: Thiết lập các biến ngẫu nhiên để thay đổi bài toán
            lis_q_max = [6, 7]  # Tập Q sẽ từ {1..6} hoặc {1..7}
            q_max = random.choice(lis_q_max)
            Q_set = list(range(1, q_max + 1))

            # Chọn tổng S sao cho luôn có ít nhất vài bộ số thỏa mãn
            if q_max == 6:
                target_sum = random.randint(9, 11)
            else:
                target_sum = random.randint(10, 13)

            # Tìm các bộ 3 chữ số khác nhau trong Q có tổng bằng target_sum
            combinations = []
            for i in range(0, len(Q_set)):
                for j in range(i + 1, len(Q_set)):
                    for k in range(j + 1, len(Q_set)):
                        if Q_set[i] + Q_set[j] + Q_set[k] == target_sum:
                            combinations.append((Q_set[i], Q_set[j], Q_set[k]))

            # Tính số phần tử của biến cố
            count_sets = len(combinations)
            ans_value = count_sets * 6  # Mỗi bộ 3 chữ số khác nhau có 3! = 6 cách sắp xếp

            # B4: Tạo các phương án sai không trùng với đáp án đúng
            kq_dung = ans_value
            wrong_choices = set()
            while len(wrong_choices) < 3:
                fake = kq_dung + random.choice([-12, -6, 6, 12, 18, -4, 4])
                if fake > 0 and fake != kq_dung:
                    wrong_choices.add(fake)

            list_wrong = list(wrong_choices)

            # Chuẩn bị nội dung câu hỏi
            noidungcauhoi = ('''Cho tập $Q = \\left\\{1; 2; 3; \\dots; %s \\right\\}$. Từ tập $Q$ có thể lập được bao nhiêu số tự nhiên có $3$ chữ số khác nhau. Số phần tử của biến cố sao cho tổng $3$ chữ số bằng $%s$ là bao nhiêu?'''
                            % (latex(q_max), latex(target_sum)))

            # Chuẩn bị nội dung lời giải chi tiết
            loigiai_parts = []
            for combo in combinations:
                loigiai_parts.append('%s + %s + %s = %s' % (combo[0], combo[1], combo[2], target_sum))

            loigiai_str = '; '.join(loigiai_parts)

            loigiai = ('''Gọi $A$ là biến cố: "số tự nhiên có tổng $3$ chữ số bằng $%s$". \\\\
                        Ta có các bộ ba chữ số có tổng bằng $%s$ từ tập $Q$ là: \\\\
                        $%s$. \\\\
                        Vì mỗi bộ chữ số có $3! = 6$ cách sắp xếp để tạo thành một số tự nhiên có $3$ chữ số khác nhau, nên: \\\\
                        Số số tự nhiên có $3$ chữ số khác nhau có tổng bằng $%s$ là: $%s \\cdot 3! = %s$. \\\\
                        $\\Rightarrow n\\left(A\\right) = %s$.'''
                        % (latex(target_sum), latex(target_sum), loigiai_str, latex(target_sum), latex(count_sets), latex(ans_value), latex(ans_value)))
            dapan=' \\shortans[0]{$%s$} '%(latex(ans_value))
            # Các đáp án
            da_d = ('\\True $%s$' % (latex(ans_value)))
            da_s1 = ('$%s$' % (latex(list_wrong[0])))
            da_s2 = ('$%s$' % (latex(list_wrong[1])))
            da_s3 = ('$%s$' % (latex(list_wrong[2])))

            # Đưa các đáp án vào danh sách và xáo trộn
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất nội dung theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

