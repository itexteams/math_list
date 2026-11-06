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


def bt_dang13_p3_b1_c1_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Giữ nguyên cấu trúc đếm mệnh đề đúng từ bài trước
        pool = [
            ("$\\exists n \\in \\mathbb{Z} : \\sqrt{2^n + 1}$ là số nguyên", True, "Đúng, vì tồn tại $n = 3 \\in \\mathbb{Z}$ thỏa mãn $\\sqrt{2^3 + 1} = \\sqrt{9} = 3$ là một số nguyên."),
            ("Trong tam giác vuông, bình phương cạnh huyền bằng tổng bình phương hai cạnh góc vuông", True, "Đúng, đây chính là nội dung của định lý Pitago trong hình học phẳng."),
            ("Mọi số tự nhiên chia hết cho $2$ và $3$ thì chia hết cho $6$", True, "Đúng, vì $2$ và $3$ là hai số nguyên tố cùng nhau, một số chia hết cho cả $2$ và $3$ thì chắc chắn chia hết cho $2 \\cdot 3 = 6$."),
            ("Với $a \\in \\mathbb{N} : a \\vdots 3 \\Leftrightarrow a \\vdots 9$", False, "Sai, vì mệnh đề kéo theo chiều xuôi là sai. Ví dụ với $a = 3 \\in \\mathbb{N}$ ta có $3 \\vdots 3$ đúng nhưng $3 \\vdots 9$ sai."),
            ("$\\forall n \\in \\mathbb{N} : n^2 > 0$", False, "Sai, vì với $n = 0 \\in \\mathbb{N}$ ta có $0^2 = 0$ không lớn hơn $0$."),
            ("Một tam giác là tam giác vuông khi và chỉ khi đường trung tuyến ứng với cạnh huyền bằng một nửa cạnh huyền", True, "Đúng, đây là một tính chất và dấu hiệu nhận biết tam giác vuông quen thuộc trong hình học.")
        ]

        # Trộn đề ngẫu nhiên (chọn đủ 6 câu để khớp nội dung ảnh sửa lỗi của bạn)
        chosen_items = random.sample(pool, 6)

        # Tính toán số lượng mệnh đề đúng
        kq_num = sum(1 for item in chosen_items if item[1] is True)
        da = '$%s$' % latex(kq_num)

        # Tạo các phương án sai xung quanh đáp án đúng
        s_candi = list(range(0, 7))
        if kq_num in s_candi:
            s_candi.remove(kq_num)

        s = []
        for val in random.sample(s_candi, 3):
            s.append('$%s$' % latex(val))

        das1 = s[0]
        das2 = s[1]
        das3 = s[2]

        # Tạo chuỗi danh sách các mệnh đề hiển thị trong câu hỏi công thức chuẩn hóa $...$
        list_str_statements = ""
        for i, item in enumerate(chosen_items):
            list_str_statements += "(%s) %s. \\\\" % (latex(i + 1), item[0])
        list_str_statements = list_str_statements.rstrip(" \\\\")

        # Câu hỏi
        noidungcauhoi = ('''Cho các mệnh đề sau: \\\\ %s \\\\ Có bao nhiêu mệnh đề đúng trong các mệnh đề trên?'''
                            % (list_str_statements))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Tạo chuỗi lời giải chi tiết (đã sửa toàn bộ dấu $...$ bao quanh ký hiệu toán học)
        loigiai_chi_tiet = ""
        for i, item in enumerate(chosen_items):
            tr_fa = "đúng" if item[1] else "sai"
            loigiai_chi_tiet += "Mệnh đề (%s): \"%s\" là mệnh đề %s. %s \\\\" % (latex(i + 1), item[0], tr_fa, item[2])
        loigiai_chi_tiet = loigiai_chi_tiet.rstrip(" \\\\")

        loigiai = ('''Xét tính đúng sai của từng mệnh đề ta có: \\\\ %s \\\\ Kết luận: Có tất cả $%s$ mệnh đề đúng.'''
                    % (loigiai_chi_tiet, latex(kq_num)))
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq_num))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
    return content

