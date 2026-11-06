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


def bt_dang30_p1_b1_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1', '2']
    dang = random.choice(lisdang)

    # Chọn ngẫu nhiên tên điểm giao cắt
    points = ['I', 'J', 'K', 'H', 'E', 'F']
    I_pt = random.choice(points)

    if dang == '1':
        # Dạng 1: MP cắt NQ
        noidungcauhoi = ('''Cho tứ diện $ABCD$. Gọi $M, N$ lần lượt là trung điểm $AB$ và $CD$. Mặt phẳng $(\\alpha)$ qua $MN$ cắt $AD$ và $BC$ lần lượt tại $P, Q$. Biết $MP$ cắt $NQ$ tại $%s$. Ba điểm nào sau đây thẳng hàng?''' % (I_pt))

        da_d_str = '$%s, B, D$' % (I_pt)
        da_s1_str = '$%s, A, C$' % (I_pt)
        da_s2_str = '$%s, A, B$' % (I_pt)
        da_s3_str = '$%s, C, D$' % (I_pt)

        loigiai = ('''Trong mặt phẳng $(\\alpha)$, ta có $%s = MP \\cap NQ$.\\\\
    Mặt khác, ta có $MP \\subset (ABD)$ và $NQ \\subset (BCD)$.\\\\
    Do đó, $%s \\in (ABD) \\cap (BCD)$.\\\\
    Mà $(ABD) \\cap (BCD) = BD$.\\\\
    Suy ra $%s \\in BD$.\\\\
    Vậy ba điểm $%s, B, D$ thẳng hàng.''' % (I_pt, I_pt, I_pt, I_pt))

    elif dang == '2':
        # Dạng 2: MQ cắt NP (thì giao điểm sẽ thuộc AC)
        noidungcauhoi = ('''Cho tứ diện $ABCD$. Gọi $M, N$ lần lượt là trung điểm $AB$ và $CD$. Mặt phẳng $(\\alpha)$ qua $MN$ cắt $AD$ và $BC$ lần lượt tại $P, Q$. Biết $MQ$ cắt $NP$ tại $%s$. Ba điểm nào sau đây thẳng hàng?''' % (I_pt))

        da_d_str = '$%s, A, C$' % (I_pt)
        da_s1_str = '$%s, B, D$' % (I_pt)
        da_s2_str = '$%s, A, B$' % (I_pt)
        da_s3_str = '$%s, C, D$' % (I_pt)

        loigiai = ('''Trong mặt phẳng $(\\alpha)$, ta có $%s = MQ \\cap NP$.\\\\
    Mặt khác, ta có $MQ \\subset (ABC)$ và $NP \\subset (ACD)$.\\\\
    Do đó, $%s \\in (ABC) \\cap (ACD)$.\\\\
    Mà $(ABC) \\cap (ACD) = AC$.\\\\
    Suy ra $%s \\in AC$.\\\\
    Vậy ba điểm $%s, A, C$ thẳng hàng.''' % (I_pt, I_pt, I_pt, I_pt))

    # Các đáp án
    da_d = ('\\True ' + str(da_d_str))
    da_s1 = str(da_s1_str)
    da_s2 = str(da_s2_str)
    da_s3 = str(da_s3_str)

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
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

