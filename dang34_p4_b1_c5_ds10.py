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


def bt_dang34_p4_b1_c5_ds10(self):
            # Khai báo biến
            # Ta sẽ random n trong khoảng {6, 8, 10} để đảm bảo tính cân bằng giữa số chẵn và lẻ.
            n = random.choice([6, 8]) # Chọn n=6 hoặc n=8 để con số không quá lớn
            so_chan = n // 2
            so_le = n // 2
            so_con_lai = n - 2


            # n-2 vị trí còn lại có (n-2)! cách chọn
            giai_thua_con_lai = math.factorial(so_con_lai)
            kq_nguyen = so_chan * so_le * giai_thua_con_lai

            # B4: Điều chỉnh các phương án sai
            da_dung = '$%s$' % (latex(kq_nguyen))
            s_sai = set()
            while len(s_sai) < 3:
                # Tạo các đáp án sai bằng cách thay đổi các thừa số hoặc cộng trừ ngẫu nhiên
                sai = random.choice([
                    (so_chan + 1) * so_le * giai_thua_con_lai,
                    so_chan * (so_le - 1) * giai_thua_con_lai,
                    so_chan * so_le * math.factorial(so_con_lai - 1) if so_con_lai > 1 else kq_nguyen + 10,
                    kq_nguyen + random.randint(10, 100),
                    kq_nguyen - random.randint(10, 100)
                ])
                if sai != kq_nguyen and sai > 0:
                    s_sai.add('$%s$' % (latex(sai)))

            list_sai = list(s_sai)

            # Nội dung câu hỏi
            tap_hop = '{1; 2; 3; \\dots; %s}' % (n)
            noidungcauhoi = ('''Từ tập $A = \\{%s\\}$ tìm số các số gồm $%s$ chữ số đôi một khác nhau sao cho chữ số đầu là chữ số chẵn và chữ số đứng cuối là chữ số lẻ.'''
                             % (tap_hop, latex(n)))

            # Các đáp án
            da_d = '\\True ' + str(da_dung)
            da_s1 = str(list_sai[0])
            da_s2 = str(list_sai[1])
            da_s3 = str(list_sai[2])

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # B2: Viết lại lời giải chi tiết
            # Tạo chuỗi tích giai thừa cho lời giải (ví dụ: 6.5.4.3.2.1)
            chuoi_tich = ".".join([str(i) for i in range(so_con_lai, 0, -1)])

            loigiai = ('''Gọi số cần lập có dạng $\\overline{a_1a_2\\dots a_{%s}}$ với $a_i \\in A$ và đôi một khác nhau. \\\\
            Vì chữ số đứng đầu $a_1$ là chữ số chẵn nên $a_1$ có $%s$ cách chọn (từ tập các chữ số chẵn $\\{2; 4; \\dots\\}$). \\\\
            Vì chữ số đứng cuối $a_{%s}$ là chữ số lẻ nên $a_{%s}$ có $%s$ cách chọn (từ tập các chữ số lẻ $\\{1; 3; \\dots\\}$). \\\\
            Các số còn lại ($%s$ vị trí) có $%s$ cách chọn. \\\\
            Vậy có $%s \\cdot %s \\cdot (%s) = %s$ số thỏa mãn yêu cầu bài toán.'''
                       % (latex(n), latex(so_chan), 
                          latex(n), latex(n), latex(so_le), 
                          latex(so_con_lai), latex(chuoi_tich),
                          latex(so_chan), latex(so_le), latex(chuoi_tich), latex(kq_nguyen)))

            # Xuất câu trắc nghiệm theo mẫu content
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

