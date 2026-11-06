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


def bt_dang31_p1_b1_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1', '2']
    dang = random.choice(lisdang)

    if dang == '1':
        # Dạng 1: Hỏi khẳng định sai giống hệt đề gốc
        noidungcauhoi = "Trong các khẳng định sau, khẳng định nào \\textbf{sai}?"

        # Khẳng định sai (đáp án đúng của câu hỏi)
        da_d_text = "Có một và chỉ một mặt phẳng đi qua ba điểm phân biệt"

        # Các khẳng định đúng (đáp án nhiễu)
        da_s_list = [
            "Tồn tại bốn điểm không cùng thuộc một mặt phẳng",
            "Hai mặt phẳng phân biệt có một điểm chung thì chúng có một đường thẳng chung duy nhất chứa tất cả các điểm chung của hai mặt phẳng đó",
            "Có một và chỉ một đường thẳng đi qua hai điểm phân biệt cho trước"
        ]

        # Định dạng đáp án
        da_d = '\\True ' + da_d_text
        da_s1 = da_s_list[0]
        da_s2 = da_s_list[1]
        da_s3 = da_s_list[2]

        # Nội dung lời giải
        loigiai = ('''Khẳng định sai là "Có một và chỉ một mặt phẳng đi qua ba điểm phân biệt" vì theo tính chất thừa nhận của hình học không gian, có một và chỉ một mặt phẳng đi qua ba điểm \\textbf{không thẳng hàng}. Nếu ba điểm phân biệt thẳng hàng thì có vô số mặt phẳng đi qua chúng.''')

    elif dang == '2':
        # Dạng 2: Hỏi khẳng định đúng
        noidungcauhoi = "Trong các khẳng định sau về hình học không gian, khẳng định nào \\textbf{đúng}?"

        # Khẳng định đúng (đáp án đúng của câu hỏi) - Lấy từ tính chất chuẩn
        da_d_text = "Có một và chỉ một mặt phẳng đi qua ba điểm không thẳng hàng"

        # Các khẳng định sai (đáp án nhiễu)
        da_s_list = [
            "Có một và chỉ một mặt phẳng đi qua ba điểm phân biệt",
            "Hai mặt phẳng phân biệt có một điểm chung thì chúng có thể không có điểm chung nào khác",
            "Qua ba điểm phân biệt luôn xác định duy nhất một mặt phẳng"
        ]

        # Định dạng đáp án
        da_d = '\\True ' + da_d_text
        da_s1 = da_s_list[0]
        da_s2 = da_s_list[1]
        da_s3 = da_s_list[2]

        # Nội dung lời giải
        loigiai = ('''Khẳng định đúng là "Có một và chỉ một mặt phẳng đi qua ba điểm không thẳng hàng".\\\\
    Các khẳng định sai:\\\\
    - "Có một và chỉ một mặt phẳng đi qua ba điểm phân biệt": Sai, vì nếu 3 điểm thẳng hàng thì có vô số mặt phẳng.\\\\
    - "Qua ba điểm phân biệt luôn xác định duy nhất một mặt phẳng": Sai, tương tự như trên.\\\\
    - "Hai mặt phẳng phân biệt có một điểm chung thì chúng có thể không có điểm chung nào khác": Sai, vì nếu có 1 điểm chung thì chúng sẽ có 1 đường thẳng chung duy nhất chứa tất cả các điểm chung.''')

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choice \n'
        '{'+str(list_1[0])+'}\n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n\\end{minipage} \n\n')
    return content

