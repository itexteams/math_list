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


def bt_dang52_p3_b2_c5_ds10(self):
            while True:
                # n tối đa là 40 để C(n, 3) < 9999
                n = random.randint(5, 40)

                # Tính giá trị số tự nhiên của C_n^3
                kq_val = math.comb(n, 3)

                if kq_val < 9999:
                    break

            # Đáp án đúng dạng số tự nhiên
            da_dung_str = '$%s$' % latex(kq_val)

            # Bước 4: Tạo các phương án sai (số tự nhiên)
            s_set = set()
            while len(s_set) < 3:
                # Các bẫy: Tổ hợp C_n^2, chỉnh hợp A_n^3, hoặc sai lệch đơn vị
                sai_cn2 = math.comb(n, 2)
                sai_an3 = math.perm(n, 3)
                offset = random.choice([10, -10, 5, -5, 20, 100])

                # Chọn ngẫu nhiên kiểu sai (khống chế không để số quá lớn hoặc âm)
                nhieu_val = random.choice([sai_cn2, kq_val + offset, n*3])

                if nhieu_val > 0 and nhieu_val != kq_val:
                    s_set.add('$%s$' % latex(nhieu_val))

            list_ans = ['\\True ' + da_dung_str] + list(s_set)
            random.shuffle(list_ans)

            # Câu hỏi
            noidungcauhoi = ('''Trong mặt phẳng cho tập hợp $P$ gồm $%s$ điểm phân biệt trong đó không có $3$ điểm nào thẳng hàng. Số tam giác có $3$ đỉnh đều thuộc tập hợp $P$ bằng bao nhiêu?'''
                             % (latex(n)))

            # Nội dung lời giải chi tiết
            loigiai = ('''Để tạo thành một tam giác, ta cần chọn ra $3$ điểm không thẳng hàng từ tập hợp điểm đã cho. \\\\
                         Theo giả thiết, tập hợp $P$ gồm $%s$ điểm phân biệt và không có $3$ điểm nào thẳng hàng. \\\\
                         Do đó, mỗi cách chọn $3$ điểm từ $%s$ điểm của tập hợp $P$ sẽ tạo thành đúng $1$ tam giác. \\\\
                         Số tam giác tạo thành là số tổ hợp chập $3$ của $%s$ phần tử: \\\\
                         $C_{%s}^3 = \\dfrac{%s \\cdot %s \\cdot %s}{3 \\cdot 2 \\cdot 1} = %s$ (tam giác).'''
                       % (latex(n), latex(n), latex(n), latex(n), latex(n), latex(n-1), latex(n-2), latex(kq_val)))

            # Đáp án ngắn (đã sửa từ n sang kq_val)
            dapan = '\\shortans[0]{$%s$}\n' % (latex(kq_val))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')

            return content

