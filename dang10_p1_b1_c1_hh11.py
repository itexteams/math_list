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


def bt_dang10_p1_b1_c1_hh11(self):
            # Khai báo biến
            questions_data = {
                '1': { # Dạng 1: Đặc điểm Mặt bên
                    'noidungcauhoi': '''Trong các phát biểu sau đây về hình chóp, phát biểu nào đúng?''',
                    'da_dung': "Tất cả các mặt bên của hình chóp là hình tam giác",
                    'da_sai_1': "Hình chóp có tất cả các mặt là hình tam giác",
                    'da_sai_2': "Tồn tại một mặt bên của hình chóp không phải là hình tam giác",
                    'da_sai_3': "Số cạnh bên của hình chóp bằng số mặt của nó",
                    'loigiai': '''Theo định nghĩa về hình chóp, tất cả các mặt bên được tạo thành bởi đỉnh chóp $S$ và các cạnh đáy là các hình tam giác. \\\\
                                 - Phương án "Hình chóp có tất cả các mặt là hình tam giác" là sai, vì mặt đáy là một đa giác.\\\\
                                 - Phương án "Tồn tại một mặt bên của hình chóp không phải là hình tam giác" là sai, vì tất cả các mặt bên phải là tam giác.\\\\
                                 - Phương án "Số cạnh bên của hình chóp bằng số mặt của nó" là sai. Nếu đáy có $n$ cạnh, số mặt là $n+1$.\\\\
                                 Vậy, phát biểu đúng là Tất cả các mặt bên của hình chóp là hình tam giác.'''
                },
                '2': { # Dạng 2: Đặc điểm Đáy và Đỉnh
                    'noidungcauhoi': '''Trong các phát biểu sau đây về hình chóp, phát biểu nào sai?''',
                    'da_dung': "Hình chóp chỉ có một mặt phẳng đối xứng",
                    'da_sai_1': "Mặt đáy của hình chóp là một đa giác",
                    'da_sai_2': "Các mặt bên của hình chóp luôn có chung một đỉnh",
                    'da_sai_3': "Hình chóp có $n$ mặt bên khi đáy là đa giác $n$ cạnh",
                    'loigiai': '''Theo định nghĩa và tính chất của hình chóp:\\\\
                                 - Các phương án 1, 2, 4 đều đúng theo định nghĩa.\\\\
                                 - Phương án "Hình chóp chỉ có một mặt phẳng đối xứng" là sai. Số lượng mặt phẳng đối xứng của hình chóp phụ thuộc vào hình dạng của hình chóp. Ví dụ, hình chóp tứ giác đều có 4 mặt phẳng đối xứng.'''
                },
                '3': { # Dạng 3: Số lượng các thành phần
                    'noidungcauhoi': '''Một hình chóp có đáy là đa giác $n$ cạnh. Số lượng các mặt của hình chóp đó là:''',
                    'da_dung': "$n+1$ mặt",
                    'da_sai_1': "$n$ mặt",
                    'da_sai_2': "$2n$ mặt",
                    'da_sai_3': "$n+2$ mặt",
                    'loigiai': '''Hình chóp có đáy là đa giác $n$ cạnh sẽ có:\\\\
                                 - $n$ mặt bên (tương ứng với $n$ cạnh đáy).\\
                                 - 1 mặt đáy.\\\\
                                 Tổng số mặt là $n$ (mặt bên) $+ 1$ (mặt đáy) $= n+1$ mặt.'''
                }
            }

            # Chọn ngẫu nhiên một dạng câu hỏi
            lisdang = list(questions_data.keys())
            dang = random.choice(lisdang)
            data = questions_data[dang]

            # Lấy dữ liệu từ dạng đã chọn
            noidungcauhoi = data['noidungcauhoi']
            da_dung = data['da_dung']
            da_sai_1 = data['da_sai_1']
            da_sai_2 = data['da_sai_2']
            da_sai_3 = data['da_sai_3']
            loigiai = data['loigiai']

            # ------------------- XỬ LÝ ĐÁP ÁN -------------------
            # Định dạng các đáp án cho file xuất, đánh dấu đáp án đúng
            da_d = ('\\True ' + da_dung)
            da_s1 = da_sai_1
            da_s2 = da_sai_2 
            da_s3 = da_sai_3 

            # Đưa các đáp án vào 1 danh sách và XÁO TRỘN NGẪU NHIÊN
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)

            # --- XUẤT CÂU TRẮC NGHIỆM RA ĐỊNH DẠNG CUỐI CÙNG (LATEX) ---
            # Sắp xếp lại thứ tự đáp án trong choice để đảm bảo thứ tự hiển thị là ngẫu nhiên (dựa vào list_1 đã shuffle)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

