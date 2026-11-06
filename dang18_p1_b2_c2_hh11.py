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


def bt_dang18_p1_b2_c2_hh11(self):
            # Khai báo biến
            # B1 & B3: Nghiên cứu đề bài và thiết lập biến ngẫu nhiên
            # Chọn ngẫu nhiên tên đường thẳng và mặt phẳng để bài toán phong phú
            ds_duong_thang = ['a', 'b', 'd', '\\Delta']
            ds_mat_phang = ['(P)', '(Q)', '(\\alpha)', '(\\beta)']

            dt1 = random.choice(ds_duong_thang)
            remaining_dt = [x for x in ds_duong_thang if x != dt1]
            dt2 = random.choice(remaining_dt)

            mp1 = random.choice(ds_mat_phang)
            remaining_mp = [x for x in ds_mat_phang if x != mp1]
            mp2 = random.choice(remaining_mp)

            # B2 & B4: Viết lại bài toán và điều chỉnh phương án
            # Câu hỏi
            noidungcauhoi = "Mệnh đề nào đúng trong các mệnh đề sau đây?"

            # Đáp án đúng (D)
            da_d = "\\True Góc giữa đường thẳng và mặt phẳng bằng góc giữa đường thẳng đó và hình chiếu của nó trên mặt phẳng đã cho"

            # Các đáp án sai (A, B, C)
            da_s1 = "Góc giữa đường thẳng $%s$ và mặt phẳng $%s$ bằng góc giữa đường thẳng $%s$ và mặt phẳng $%s$ thì mặt phẳng $%s$ song song hoặc trùng với mặt phẳng $%s$" % (dt1, mp1, dt1, mp2, mp1, mp2)
            da_s2 = "Góc giữa đường thẳng $%s$ và mặt phẳng $%s$ bằng góc giữa đường thẳng $%s$ và mặt phẳng $%s$ thì đường thẳng $%s$ song song với đường thẳng $%s$" % (dt1, mp1, dt2, mp1, dt1, dt2)
            da_s3 = "Góc giữa đường thẳng $%s$ và mặt phẳng $%s$ bằng góc giữa đường thẳng $%s$ và mặt phẳng $%s$ thì đường thẳng $%s$ song song hoặc trùng với đường thẳng $%s$" % (dt1, mp1, dt2, mp1, dt1, dt2)

            # Đưa các đáp án vào danh sách và xáo trộn
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải chi tiết
            loigiai = ("Dựa trên định nghĩa về góc giữa đường thẳng và mặt phẳng trong không gian:\\\\ "
                       "Nếu đường thẳng vuông góc với mặt phẳng thì góc giữa chúng bằng $90^\\circ$.\\\\ "
                       "Trong trường hợp đường thẳng không vuông góc với mặt phẳng, góc giữa đường thẳng và mặt phẳng là góc giữa đường thẳng đó và hình chiếu của nó trên mặt phẳng đã cho. \\\\"
                       "Do đó, mệnh đề phát biểu về mối quan hệ giữa đường thẳng và hình chiếu là mệnh đề hoàn toàn chính xác theo định nghĩa sách giáo khoa.")

            # Xuất câu trắc nghiệm (Không dùng raw string r, sử dụng double backslash)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

