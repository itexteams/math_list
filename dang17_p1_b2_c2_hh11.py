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


def bt_dang17_p1_b2_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Danh sách các khẳng định ĐÚNG trong hình học không gian (dùng làm phương án nhiễu)
                ds_khang_dinh_dung = [
                    'Nếu ba mặt phẳng cắt nhau theo ba giao tuyến phân biệt thì ba giao tuyến ấy hoặc đồng quy hoặc đôi một song song với nhau',
                    'Hai mặt phẳng phân biệt cùng vuông góc với một đường thẳng thì song song với nhau',
                    'Cho hai đường thẳng chéo nhau. Có duy nhất một mặt phẳng chứa đường thẳng này và song song với đường thẳng kia',
                    'Hai đường thẳng phân biệt cùng song song với đường thẳng thứ ba thì song song với nhau',
                    'Nếu một đường thẳng song song với một mặt phẳng thì nó song song với một đường thẳng nào đó nằm trong mặt phẳng đó'
                ]

                # Khẳng định SAI (Đáp án cần chọn theo nội dung ảnh)
                khang_dinh_sai = 'Hai đường thẳng phân biệt cùng vuông góc với một đường thẳng thì song song với nhau'

                # Cách random: Chọn ngẫu nhiên 3 khẳng định đúng từ danh sách để làm phương án sai (nhiễu)
                random.shuffle(ds_khang_dinh_dung)
                ds_nhieu = ds_khang_dinh_dung[:3]

                # Câu hỏi
                noidungcauhoi = 'Trong không gian, khẳng định nào sau đây \\textbf{sai}?'

                # Đáp án đúng của câu hỏi (là nội dung sai về mặt toán học)
                da_d = ('\\True ' + khang_dinh_sai)

                # Các đáp án nhiễu
                da_s1 = ds_nhieu[0]
                da_s2 = ds_nhieu[1]
                da_s3 = ds_nhieu[2]

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên vị trí A, B, C, D
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết, không viết tắt, sử dụng ký hiệu // theo yêu cầu
                loigiai = ('Trong không gian, hai đường thẳng phân biệt cùng vuông góc với một đường thẳng thứ ba thì chúng có thể song song hoặc chéo nhau. \\\\ '
                           'Xét ví dụ trong hình lập phương $ABCD.A\'B\'C\'D\'$: \\\\ '
                           '+ Đường thẳng $AB$ và $AD$ cùng vuông góc với đường thẳng $AA\'$, nhưng $AB$ và $AD$ cắt nhau tại $A$. \\\\ '
                           '+ Đường thẳng $BC$ và $AA\'$ cùng vuông góc với đường thẳng $AB$, nhưng $BC$ và $AA\'$ chéo nhau trong không gian. \\\\ '
                           'Ngược lại, nếu $A\'B\' \\perp AA\'$ và $AB \\perp AA\'$ thì $A\'B\' // AB$. \\\\ '
                           'Do đó, khẳng định "Hai đường thẳng phân biệt cùng vuông góc với một đường thẳng thì song song với nhau" là khẳng định \\textbf{sai}.')

            # Xuất câu trắc nghiệm theo đúng cấu trúc mẫu (không dùng raw string)
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

