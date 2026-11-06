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


def bt_dang16_p1_b2_c2_hh11(self):
            # Khai báo biến
            # Khai báo danh sách các ký hiệu để random
            lis_duong_thang = ['d', 'a', 'b', '\\Delta', 'l']
            lis_mat_phang = ['\\alpha', '\\beta', 'P', 'Q']

            # Chọn ngẫu nhiên tên đường thẳng và mặt phẳng
            d = random.choice(lis_duong_thang)
            alpha = random.choice(lis_mat_phang)
            # Chọn đường thẳng phụ a khác với d
            a = random.choice([x for x in lis_duong_thang if x != d])

            # Định nghĩa các khẳng định với định dạng $...$ và \left( \right)
            # Khẳng định A (Đúng)
            khang_dinh_A = (
                'Nếu đường thẳng $' + d + '$ vuông góc với mặt phẳng $\\left(' + alpha + '\\right)$ '
                'thì $' + d + '$ vuông góc với hai đường thẳng trong mặt phẳng $\\left(' + alpha + '\\right)$'
            )

            # Khẳng định B (Sai - Đáp án)
            khang_dinh_B = (
                'Nếu đường thẳng $' + d + '$ vuông góc với hai đường thẳng nằm trong mặt phẳng $\\left(' + alpha + '\\right)$ '
                'thì $' + d + '$ vuông góc với mặt phẳng $\\left(' + alpha + '\\right)$'
            )

            # Khẳng định C (Đúng)
            khang_dinh_C = (
                'Nếu đường thẳng $' + d + '$ vuông góc với hai đường thẳng cắt nhau nằm trong mặt phẳng $\\left(' + alpha + '\\right)$ '
                'thì $' + d + '$ vuông góc với bất kỳ đường thẳng nào nằm trong mặt phẳng $\\left(' + alpha + '\\right)$'
            )

            # Khẳng định D (Đúng) - Sử dụng ký hiệu //
            khang_dinh_D = (
                'Nếu $' + d + ' \\perp \\left(' + alpha + '\\right)$ và đường thẳng $' + a + ' // \\left(' + alpha + '\\right)$ '
                'thì $' + d + ' \\perp ' + a + '$'
            )

            # Câu hỏi
            noidungcauhoi = 'Khẳng định nào sau đây SAI?'

            # Các đáp án
            da_d = ('\\True ' + khang_dinh_B)
            da_s1 = khang_dinh_A
            da_s2 = khang_dinh_C
            da_s3 = khang_dinh_D

            # Trộn ngẫu nhiên các phương án
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải chi tiết
            loigiai = (
                'Khẳng định B là khẳng định SAI vì: \\\\ '
                'Theo định lý về điều kiện để đường thẳng vuông góc với mặt phẳng, đường thẳng $' + d + '$ '
                'phải vuông góc với hai đường thẳng cắt nhau cùng nằm trong mặt phẳng $\\left(' + alpha + '\\right)$ '
                'thì $' + d + '$ mới vuông góc với mặt phẳng $\\left(' + alpha + '\\right)$. \\\\ '
                'Nếu $' + d + '$ vuông góc với hai đường thẳng nằm trong $\\left(' + alpha + '\\right)$ '
                'mà hai đường thẳng đó song song với nhau thì $' + d + '$ chưa chắc đã vuông góc với mặt phẳng $\\left(' + alpha + '\\right)$.'
            )

            # Xuất nội dung theo cấu trúc mẫu (Không dùng tiền tố r)
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

