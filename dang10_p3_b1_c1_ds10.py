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


def bt_dang10_p3_b1_c1_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Định nghĩa danh sách toàn bộ 8 mệnh đề kèm theo tính sai (True nếu mệnh đề sai, False nếu mệnh đề đúng) và lời giải tương ứng
        # Mỗi phần tử: (Chuỗi mệnh đề, Mệnh đề này SAI? (True/False), Chuỗi giải thích)
        pool = [
            ("\\forall x \\in \\mathbb{R}, x^3 < 3x", True, "Sai, vì với $x = 2 \\in \\mathbb{R}$ ta có $2^3 = 8 > 3 \\cdot 2 = 6$."),
            ("\\exists x \\in \\mathbb{Z}, x^2 \\neq 17", False, "Đúng, vì với $x = 1 \\in \\mathbb{Z}$ ta có $1^2 = 1 \\neq 17$."),
            ("\\exists x \\in \\mathbb{R}, x^2 + 4 < 4x", True, "Sai, vì biến đổi tương đương thành $(x-2)^2 < 0$ (vô lý với mọi $x \\in \\mathbb{R}$)."),
            ("\\exists x \\in \\mathbb{N}, 3x^2 - 2x - 5 = 0", False, "Đúng, vì phương trình có nghiệm thực $x = -1$ và $x = \\frac{5}{3}$ nhưng cả hai nghiệm này đều không thuộc $\\mathbb{N}$ (mệnh đề gốc trong ảnh là sai, do đó phủ định tính đúng sai gốc: mệnh đề này Sai). Vui lòng kiểm tra lại nghiệm: $3(-1)^2 - 2(-1) - 5 = 0$, nghiệm còn lại là $\\frac{5}{3}$. Vì cả hai không thuộc $\\mathbb{N}$ nên mệnh đề này Sai."),
            ("\\forall x \\in \\mathbb{R}, x^2 > 0", True, "Sai, vì với $x = 0 \\in \\mathbb{R}$ ta có $0^2 = 0$ không lớn hơn $0$."),
            ("\\exists x \\in \\mathbb{N}, x^2 + 4x + 3 = 0", True, "Sai, vì phương trình có hai nghiệm $x = -1$ và $x = -3$ đều không thuộc $\\mathbb{N}$."),
            ("\\exists x \\in \\mathbb{R}, x^2 + 2x + 4 < 0", True, "Sai, vì $x^2 + 2x + 4 = (x+1)^2 + 3 \\ge 3 > 0$ với mọi $x \\in \\mathbb{R}$."),
            ("\\exists x \\in \\mathbb{R}, x^2 \\le 0", False, "Đúng, vì tồn tại $x = 0 \\in \\mathbb{R}$ thỏa mãn $0^2 \\le 0$.")
        ]

        # Để sửa lại logic chính xác tuyệt đối cho câu số 4: 
        # Nghiệm của 3x^2 - 2x - 5 = 0 là x = -1 và x = 5/3. Cả hai đều không thuộc N. Vậy mệnh đề gốc SAI.
        pool[3] = ("\\exists x \\in \\mathbb{N}, 3x^2 - 2x - 5 = 0", True, "Sai, vì phương trình có nghiệm $x = -1$ và $x = \\frac{5}{3}$ đều không thuộc tập hợp số tự nhiên $\\mathbb{N}$.")

        # Chọn ngẫu nhiên từ 5 đến 7 mệnh đề để tạo sự đa dạng cho đề bài
        num_select = random.randint(5, 7)
        chosen_items = random.sample(pool, num_select)

        # Đếm số lượng mệnh đề SAI
        kq_num = sum(1 for item in chosen_items if item[1] is True)
        da = '$%s$' % latex(kq_num)

        # Tạo các phương án sai (từ 0 đến num_select và không trùng với kq_num)
        s_candi = list(range(0, num_select + 1))
        if kq_num in s_candi:
            s_candi.remove(kq_num)

        s = []
        for val in random.sample(s_candi, 3):
            s.append('$%s$' % latex(val))

        das1 = s[0]
        das2 = s[1]
        das3 = s[2]

        # Tạo chuỗi danh sách các mệnh đề hiển thị trong câu hỏi
        list_str_statements = ""
        for i, item in enumerate(chosen_items):
            list_str_statements += "%s. $%s$ \\\\" % (latex(i + 1), item[0])
        list_str_statements = list_str_statements.rstrip(" \\\\")

        # Câu hỏi
        noidungcauhoi = ('''Trong các mệnh đề sau đây, có bao nhiêu mệnh đề sai? \\\\ %s'''
                            % (list_str_statements))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào danh sách và trộn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Tạo chuỗi lời giải chi tiết từng bước
        loigiai_chi_tiet = ""
        for i, item in enumerate(chosen_items):
            tr_fa = "sai" if item[1] else "đúng"
            loigiai_chi_tiet += "Mệnh đề %s: $%s$ là mệnh đề %s. %s \\\\" % (latex(i + 1), item[0], tr_fa, item[2])
        loigiai_chi_tiet = loigiai_chi_tiet.rstrip(" \\\\")

        loigiai = ('''Xét tính đúng sai của từng mệnh đề ta có: \\\\ %s \\\\ Kết luận: Có tất cả $%s$ mệnh đề sai.'''
                    % (loigiai_chi_tiet, latex(kq_num)))
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq_num))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) +dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
    return content

