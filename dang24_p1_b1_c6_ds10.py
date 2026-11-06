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


def bt_dang24_p1_b1_c6_ds10(self):
            # Khai báo biến
            # B3: Suy nghĩ tìm cách random bài toán (Random số lần gieo n)
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random số lần gieo đồng xu từ 3 đến 5 lần để đa dạng đề bài
                n = random.randint(3, 5) 

                # Định nghĩa các thành phần biến cố
                # Trong bài: A_i là mặt sấp -> gạch đầu A_i là mặt ngửa
                loai_mat_chinh = "sấp"
                loai_mat_doi = "ngửa"

                # Biến số để hiển thị trong câu hỏi và lời giải
                day_bien_co = " \\cup ".join(["\\overline{A_{%s}}" % i for i in range(1, n + 1)])
                day_loi_giai = " hoặc ".join(["mặt %s xuất hiện ở lần gieo thứ %s" % (loai_mat_doi, i) for i in range(1, n + 1)])

                # Đáp án đúng
                da_dung = "Mặt %s xuất hiện ít nhất một lần" % loai_mat_doi

                # Các phương án sai (B4: Đảm bảo không trùng với đáp án đúng)
                s = [
                    "Cả %s lần gieo đều được mặt %s" % (n, loai_mat_chinh),
                    "Mặt %s xuất hiện không quá một lần" % loai_mat_chinh,
                    "Cả %s lần gieo đều được mặt %s" % (n, loai_mat_doi),
                    "Mặt %s xuất hiện đúng một lần" % loai_mat_doi,
                    "Mặt %s không xuất hiện lần nào" % loai_mat_doi
                ]

                # Trộn và chọn các phương án sai
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = (
                    "Gieo một đồng xu cân đối đồng chất %s lần. Gọi $A_i$ là biến cố \"mặt %s xuất hiện ở lần gieo thứ $i$\", với $i=1, 2, \\dots, %s$. Khi đó, biến cố $%s$ là"
                    % (latex(n), loai_mat_chinh, latex(n), day_bien_co)
                )

                # Các đáp án
                da_d = ("\\True " + da_dung)
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (Không viết tắt)
                loigiai = (
                    "Ta có $A_i$ là biến cố \"mặt %s xuất hiện ở lần gieo thứ $i$\".\\\\ "
                    "Suy ra $\\overline{A_i}$ là biến cố \"mặt %s xuất hiện ở lần gieo thứ $i$\".\\\\ "
                    "Biến cố $%s$ có nghĩa là: %s.\\\\ "
                    "Điều này đồng nghĩa với việc: \"Mặt %s xuất hiện ít nhất một lần\"."
                    % (loai_mat_chinh, loai_mat_doi, day_bien_co, day_loi_giai, loai_mat_doi)
                )

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\n\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

