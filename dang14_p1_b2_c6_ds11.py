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


def bt_dang14_p1_b2_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng (theo mẫu)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Chọn ngẫu nhiên xác suất của động cơ I và II
                # Đảm bảo các giá trị thực tế và dễ tính toán (0.7 đến 0.95)
                p1_val = Decimal(str(random.choice([0.7, 0.75, 0.8, 0.85, 0.9])))
                p2_val = Decimal(str(random.choice([0.9, 0.92, 0.95, 0.96])))

                # Tính các giá trị trung gian theo lời giải trong ảnh
                p_inter_val = p1_val * p2_val # P(I.II)
                kq_val = p1_val + p2_val - p_inter_val # P(I U II)

                # Chuyển định dạng dấu . thành dấu , cho phù hợp yêu cầu tiếng Việt
                p1 = str(p1_val).replace('.', ',')
                p2 = str(p2_val).replace('.', ',')
                p_inter = str(p_inter_val).replace('.', ',')
                kq = str(kq_val).replace('.', ',')

                # Bước 4: Điều chỉnh các phương án sai không được trùng với đáp án đúng
                # Tạo danh sách đáp án sai
                s = set()
                # Sai lầm 1: Chỉ lấy tích (P(I.II))
                s.add(str(p_inter_val).replace('.', ','))
                # Sai lầm 2: Chỉ lấy p2 (hoặc p1)
                s.add(str(p2_val).replace('.', ','))
                # Sai lầm 3: Tổng trừ đi một giá trị khác hoặc cộng nhầm
                fake1 = p1_val * Decimal('0.95') # Một giá trị xác suất ngẫu nhiên khác
                s.add(str(fake1.quantize(Decimal('0.000'), rounding=ROUND_HALF_UP)).replace('.', ','))

                # Nếu trùng với đáp án đúng, xóa và thêm giá trị khác
                if kq in s:
                    s.remove(kq)

                # Đảm bảo có đủ 3 đáp án sai khác biệt
                while len(s) < 3:
                    fake_val = kq_val - Decimal('0.04')
                    s.add(str(fake_val).replace('.', ','))

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi (B2: Viết lại y hệt bài toán theo mẫu)
                noidungcauhoi = (
                    "Một tổ hợp máy có hai động cơ $I$ và $II$ hoạt động độc lập nhau, xác suất động cơ $I$ hoạt động "
                    "được là $%s$, xác suất động cơ $II$ hoạt động được là $%s$. Biết tổ hợp máy chạy được "
                    "nếu ít nhất một động cơ hoạt động. Xác suất để tổ hợp máy chạy được là"
                    % (p1, p2)
                )

                # Đáp án
                da_d = "\\True " + str(kq)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết (Không viết tắt, dùng \left( \right) và dấu ,)
                loigiai = (
                    "Ta có: $P\\left( I \\right) = %s$; $P\\left( II \\right) = %s$. \\\\ "
                    "Vì động cơ $I$ và $II$ hoạt động độc lập nhau nên \\\\ "
                    "$P\\left( I \\cdot II \\right) = P\\left( I \\right) \\cdot P\\left( II \\right) = %s \\cdot %s = %s$. \\\\ "
                    "Vậy xác suất tổ hợp máy chạy được là: \\\\ "
                    "$P\\left( I \\cup II \\right) = P\\left( I \\right) + P\\left( II \\right) - P\\left( I \\cdot II \\right) = %s + %s - %s = %s$."
                    % (p1, p2, p1, p2, p_inter, p1, p2, p_inter, kq)
                )

            # Xuất câu trắc nghiệm (Không dùng raw string r)
            content = (
                "\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n" + str(noidungcauhoi) + "\n"
                "\\choice \n"
                "{" + str(list_1[0]) + "}\n"
                "{" + str(list_1[1]) + "}\n"
                "{" + str(list_1[2]) + "}\n"
                "{" + str(list_1[3]) + "}\n"
                "\\loigiai{" + str(loigiai) + "}\n"
                "\\end{ex}\n \\end{minipage} \n\n")
            return content

