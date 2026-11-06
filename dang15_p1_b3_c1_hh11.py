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


def bt_dang15_p1_b3_c1_hh11(self):
    # Khai báo biến
    lisdang=['1', '2']
    dang=random.choice(lisdang)

    if dang=='1':
        # Dạng 1: Tìm khẳng định SAI (như bài gốc)
        cau_hoi_str = "Trong các khẳng định sau, khẳng định nào %s?"
        tu_khoa = "\\textbf{sai}"

        # Ngân hàng khẳng định SAI kèm lời giải thích
        ds_khang_dinh_sai = [
            (
                "Nếu ba mặt phẳng đôi một cắt nhau theo ba giao tuyến phân biệt thì ba giao tuyến ấy đồng qui",
                "Theo định lý về giao tuyến của ba mặt phẳng: Nếu ba mặt phẳng đôi một cắt nhau theo ba giao tuyến phân biệt thì ba giao tuyến ấy hoặc đôi một song song, hoặc đồng quy. Do đó khẳng định trên thiếu trường hợp ba giao tuyến song song nên là khẳng định sai."
            ),
            (
                "Hai đường thẳng không có điểm chung thì chéo nhau",
                "Hai đường thẳng không có điểm chung có thể song song với nhau (nếu cùng thuộc một mặt phẳng) hoặc chéo nhau (nếu không cùng thuộc một mặt phẳng). Do đó khẳng định trên là sai."
            ),
            (
                "Hai đường thẳng phân biệt không cắt nhau thì song song",
                "Trong không gian, hai đường thẳng phân biệt không cắt nhau có thể song song hoặc chéo nhau. Do đó khẳng định trên là sai."
            ),
            (
                "Nếu một đường thẳng song song với một mặt phẳng thì nó song song với mọi đường thẳng nằm trong mặt phẳng đó",
                "Nếu một đường thẳng $d$ song song với mặt phẳng $(\\alpha)$ thì nó chỉ song song với các đường thẳng nằm trong $(\\alpha)$ mà đồng phẳng với $d$. Với các đường thẳng khác nằm trong $(\\alpha)$, $d$ có thể chéo nhau với chúng. Do đó khẳng định trên là sai."
            )
        ]

        # Ngân hàng các khẳng định ĐÚNG
        ds_khang_dinh_dung = [
            "Nếu hai đường thẳng song song thì chúng cùng nằm trên một mặt phẳng",
            "Có một và chỉ một mặt phẳng đi qua hai đường thẳng cắt nhau cho trước",
            "Nếu một đường thẳng song song với một mặt phẳng thì nó song song với một đường thẳng nào đó trong mặt phẳng",
            "Có một và chỉ một mặt phẳng đi qua ba điểm không thẳng hàng",
            "Nếu hai mặt phẳng phân biệt có một điểm chung thì chúng có một đường thẳng chung duy nhất đi qua điểm chung đó"
        ]

        muc_sai_duoc_chon = random.choice(ds_khang_dinh_sai)
        da = muc_sai_duoc_chon[0]
        ly_do = muc_sai_duoc_chon[1]

        # Lấy ngẫu nhiên 3 phương án đúng làm đáp án nhiễu
        cac_phuong_an_dung = random.sample(ds_khang_dinh_dung, 3)
        das1 = cac_phuong_an_dung[0]
        das2 = cac_phuong_an_dung[1]
        das3 = cac_phuong_an_dung[2]

        noidungcauhoi = (cau_hoi_str % (tu_khoa))

        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        loigiai = ('''Khẳng định sai là: "%s". \\\\
    %s''' % (da, ly_do))

    elif dang=='2':
        # Dạng 2: Tìm khẳng định ĐÚNG
        cau_hoi_str = "Trong các khẳng định sau, khẳng định nào %s?"
        tu_khoa = "\\textbf{đúng}"

        ds_khang_dinh_dung = [
            (
                "Nếu hai đường thẳng song song thì chúng cùng nằm trên một mặt phẳng",
                "Theo định nghĩa hai đường thẳng song song trong không gian: Hai đường thẳng được gọi là song song nếu chúng cùng nằm trong một mặt phẳng và không có điểm chung. Do đó khẳng định này là đúng."
            ),
            (
                "Có một và chỉ một mặt phẳng đi qua hai đường thẳng cắt nhau cho trước",
                "Theo tính chất xác định mặt phẳng: Hai đường thẳng cắt nhau xác định duy nhất một mặt phẳng chứa cả hai đường thẳng đó. Do đó khẳng định này là đúng."
            ),
            (
                "Nếu một đường thẳng song song với một mặt phẳng thì nó song song với một đường thẳng nào đó trong mặt phẳng",
                "Nếu đường thẳng $d // (\\alpha)$ thì qua $d$ có mặt phẳng $(\\beta)$ cắt $(\\alpha)$ theo giao tuyến $d'$. Khi đó $d // d'$ với $d' \\subset (\\alpha)$. Do đó khẳng định này là đúng."
            )
        ]

        ds_khang_dinh_sai = [
            "Nếu ba mặt phẳng đôi một cắt nhau theo ba giao tuyến phân biệt thì ba giao tuyến ấy đồng qui",
            "Hai đường thẳng không có điểm chung thì chéo nhau",
            "Hai đường thẳng phân biệt cùng song song với một mặt phẳng thì song song với nhau",
            "Nếu đường thẳng $a // (\\alpha)$ và $b \\subset (\\alpha)$ thì $a // b$"
        ]

        muc_dung_duoc_chon = random.choice(ds_khang_dinh_dung)
        da = muc_dung_duoc_chon[0]
        ly_do = muc_dung_duoc_chon[1]

        cac_phuong_an_sai = random.sample(ds_khang_dinh_sai, 3)
        das1 = cac_phuong_an_sai[0]
        das2 = cac_phuong_an_sai[1]
        das3 = cac_phuong_an_sai[2]

        noidungcauhoi = (cau_hoi_str % (tu_khoa))

        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        loigiai = ('''Khẳng định đúng là: "%s". \\\\
    %s''' % (da, ly_do))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
        '\\choice \n'
        '{' + str(list_1[1]) + '}\n'
        '{' + str(list_1[2]) + '}\n'
        '{' + str(list_1[3]) + '}\n'
        '{' + str(list_1[0]) + '}\n'
        '\\loigiai{' + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

