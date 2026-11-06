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


def bt_dang18_p3_b1_c1_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Sinh ngẫu nhiên giá trị giới hạn k_val từ 2 đến 10 (trong ảnh gốc là 2)
        # Ta chọn các giá trị sao cho tập nghiệm nguyên phong phú
        k_val = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10])

        # Giải bất phương trình x^2 <= k_val để tìm các nghiệm nguyên x
        # Nghiệm nguyên sẽ nằm trong đoạn [-floor(sqrt(k_val)), floor(sqrt(k_val))]
        limit_root = int(math.floor(math.sqrt(k_val)))
        elements = list(range(-limit_root, limit_root + 1))

        # Số các số nguyên thỏa mãn
        kq_num = len(elements)
        da = '$%s$' % latex(kq_num)

        # Tạo các phương án sai xung quanh đáp án đúng (không trùng với kq_num và lớn hơn 0)
        s_candi = [kq_num + 1, kq_num + 2, kq_num - 1, kq_num - 2, kq_num + 3]
        s_candi = [v for v in s_candi if v != kq_num and v > 0]

        s = []
        for val in random.sample(s_candi, 3):
            s.append('$%s$' % latex(val))

        das1 = s[0]
        das2 = s[1]
        das3 = s[2]

        # Tạo chuỗi hiển thị danh sách các nghiệm nguyên
        elements_str = "; ".join(str(x) for x in elements)

        # Câu hỏi
        noidungcauhoi = ('''Cho mệnh đề $P$: "Bình phương của một số thực lớn hơn %s". Số các số nguyên thỏa mãn mệnh đề phủ định của mệnh đề $P$ bằng bao nhiêu?'''
                            % (latex(k_val)))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Tạo nội dung lời giải chi tiết từng bước
        loigiai = ('''Ký hiệu $x$ là một số thực bất kì. Khi đó mệnh đề $P$ được biểu diễn dưới dạng ký hiệu toán học là: \\\\
    $P$: "$x^2 > %s$". \\\\
    Mệnh đề phủ định của mệnh đề $P$ (ký hiệu là $\\overline{P}$) sẽ đảo ngược dấu của bất đẳng thức trên: \\\\
    $\\overline{P}$: "$x^2 \\le %s$". \\\\
    Vì bài toán yêu cầu tìm các giá trị nguyên thỏa mãn ($x \\in \\mathbb{Z}$), ta giải bất phương trình trên tập hợp số nguyên: \\\\
    $x^2 \\le %s \\Rightarrow -\\sqrt{%s} \\le x \\le \\sqrt{%s}$. \\\\
    Do $x \\in \\mathbb{Z}$ nên ta chọn được các giá trị nguyên thỏa mãn là: $x \\in \\{%s\\}$. \\\\
    Vậy có tất cả $%s$ số nguyên thỏa mãn mệnh đề phủ định $\\overline{P}$.'''
                    % (latex(k_val), latex(k_val), latex(k_val), latex(k_val), latex(k_val), elements_str, latex(kq_num)))
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq_num))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
    return content

