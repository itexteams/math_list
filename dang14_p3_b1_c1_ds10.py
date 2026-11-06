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


def bt_dang14_p3_b1_c1_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Thiết lập tham số ngẫu nhiên cho các mệnh đề toán học
        n1 = random.choice([2, 3, 5, 7])  # Số dưới dấu căn (ví dụ gốc: 3)
        n2 = random.randint(6, 15)        # Số bị chia (ví dụ gốc: 7)
        n3 = random.randint(3, 5)         # Số chia (ví dụ gốc: 4)
        while n2 % n3 == 0:
            n2 = random.randint(6, 15)

        # Định nghĩa danh sách 5 mệnh đề từ ảnh gốc kèm tính chất SAI (True nếu mệnh đề gốc SAI -> Phủ định ĐÚNG)
        # Mọi công thức toán học phức tạp hay đơn giản đều được bao bọc chuẩn trong $...$
        pool = [
            ("$Q$ : \"$\\forall x \\in \\mathbb{R}, 2x^2 - 3x + 1 \\neq 0$\"", True, "Mệnh đề này sai vì phương trình $2x^2 - 3x + 1 = 0$ có nghiệm thực $x = 1$ hoặc $x = 0,5$. Do đó, mệnh đề phủ định của nó là đúng."),
            ("Hình bình hành có hai đường chéo luôn luôn bằng nhau", True, "Mệnh đề này sai vì hình bình hành tổng quát không có hai đường chéo bằng nhau (chỉ hình chữ nhật và hình vuông mới có tính chất này). Do đó, mệnh đề phủ định của nó là đúng."),
            ("$%s$ không chia hết cho $%s$" % (latex(n2), latex(n3)), False, "Mệnh đề này đúng vì $%s$ chia cho $%s$ có số dư khác $0$. Do đó, mệnh đề phủ định của nó là sai." % (latex(n2), latex(n3))),
            ("$P$ : \"$\\forall x \\in \\mathbb{R}, x^2 \\ge x$\"", True, "Mệnh đề này sai vì với $x = 0,5 \\in \\mathbb{R}$ ta có $0,5^2 = 0,25 < 0,5$. Do đó, mệnh đề phủ định của nó là đúng."),
            ("$\\sqrt{%s}$ là số hữu tỉ" % latex(n1), True, "Mệnh đề này sai vì $\\sqrt{%s}$ là một số vô tỉ. Do đó, mệnh đề phủ định của nó là đúng." % latex(n1))
        ]

        # Trộn ngẫu nhiên (chọn toàn bộ 5 câu để giữ nguyên cấu trúc hiển thị của ảnh lỗi)
        chosen_items = random.sample(pool, 5)

        # Đếm số lượng mệnh đề có mệnh đề phủ định đúng (mệnh đề gốc bị SAI)
        kq_num = sum(1 for item in chosen_items if item[1] is True)
        da = '$%s$' % latex(kq_num)

        # Tạo các phương án sai (từ 0 đến 5 và không trùng với kq_num)
        s_candi = list(range(0, 6))
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
            list_str_statements += "(%s) %s. \\\\" % (latex(i + 1), item[0])
        list_str_statements = list_str_statements.rstrip(" \\\\")

        # Câu hỏi
        noidungcauhoi = ('''Cho các mệnh đề sau: \\\\ %s \\\\ Có bao nhiêu mệnh đề có mệnh đề phủ định đúng?'''
                            % (list_str_statements))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Tạo chuỗi lời giải chi tiết cho từng bước với công thức đặt chuẩn trong $...$
        loigiai_chi_tiet = ""
        for i, item in enumerate(chosen_items):
            loigiai_chi_tiet += "Mệnh đề (%s): %s \\\\" % (latex(i + 1), item[2])
        loigiai_chi_tiet = loigiai_chi_tiet.rstrip(" \\\\")

        loigiai = ('''Một mệnh đề có mệnh đề phủ định đúng khi và chỉ khi mệnh đề ban đầu là một mệnh đề sai. Do đó, bài toán yêu cầu tìm số lượng mệnh đề sai trong các mệnh đề đã cho. \\\\
    Xét từng mệnh đề ta có: \\\\ %s \\\\ Kết luận: Có tất cả $%s$ mệnh đề có mệnh đề phủ định đúng.'''
                    % (loigiai_chi_tiet, latex(kq_num)))
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq_num))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
    return content

