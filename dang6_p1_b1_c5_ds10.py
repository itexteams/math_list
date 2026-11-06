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


def bt_dang6_p1_b1_c5_ds10(self):
            # Khai báo biến
            a1=['0,1,2,3,4','0,1,2,3,4,5','0,1,2,3,4,5,6','0,1,2,3,4,5,6,7','0,1,2,3,4,5,6,7,8']
            a=random.choice(a1)
            b1=[2,3,4,5]
            b=random.choice(b1)
            # Câu hỏi
            noidungcauhoi='''Từ các chữ số $%s$ có thể lập được bao nhiêu số tự nhiên gồm $%s$ chữ số đôi một khác nhau?''' %(str(a), latex(b))
            # Các đáp án
            if b==2 and a=='0,1,2,3,4':
                da_d = '\\True $16$'
                da_s1 = '$19$' 
                da_s2 = '$12$' 
                da_s3 = '$18$' 
            if b==2 and a=='0,1,2,3,4,5':
                da_d = '\\True $25$'
                da_s1 = '$29$' 
                da_s2 = '$22$' 
                da_s3 = '$28$' 
            if b==2 and a=='0,1,2,3,4,5,6':
                da_d = '\\True $36$'
                da_s1 = '$38$' 
                da_s2 = '$32$' 
                da_s3 = '$34$' 
            if b==2 and a=='0,1,2,3,4,5,6,7':
                da_d = '\\True $49$'
                da_s1 = '$42$' 
                da_s2 = '$45$' 
                da_s3 = '$44$'
            if b==2 and a=='0,1,2,3,4,5,6,7,8':
                da_d = '\\True $64$'
                da_s1 = '$62$' 
                da_s2 = '$63$' 
                da_s3 = '$61$'

            if b==3 and a=='0,1,2,3,4':
                da_d = '\\True $48$'
                da_s1 = '$43$' 
                da_s2 = '$42$' 
                da_s3 = '$49$' 
            if b==3 and a=='0,1,2,3,4,5':
                da_d = '\\True $100$'
                da_s1 = '$130$' 
                da_s2 = '$110$' 
                da_s3 = '$140$'
            if b==3 and a=='0,1,2,3,4,5,6':
                da_d = '\\True $180$'
                da_s1 = '$190$' 
                da_s2 = '$210$' 
                da_s3 = '$140$'
            if b==3 and a=='0,1,2,3,4,5,6,7':
                da_d = '\\True $294$'
                da_s1 = '$230$' 
                da_s2 = '$210$' 
                da_s3 = '$240$'
            if b==3 and a=='0,1,2,3,4,5,6,7,8':
                da_d = '\\True $448$'
                da_s1 = '$430$' 
                da_s2 = '$510$' 
                da_s3 = '$540$'
            if b==4 and a=='0,1,2,3,4':
                da_d = '\\True $96$'
                da_s1 = '$95$' 
                da_s2 = '$102$' 
                da_s3 = '$98$'  
            if b==4 and a=='0,1,2,3,4,5':
                da_d = '\\True $300$'
                da_s1 = '$350$' 
                da_s2 = '$280$' 
                da_s3 = '$330$' 
            if b==4 and a=='0,1,2,3,4,5,6':
                da_d = '\\True $720$'
                da_s1 = '$750$' 
                da_s2 = '$880$' 
                da_s3 = '$830$' 
            if b==4 and a=='0,1,2,3,4,5,6,7':
                da_d = '\\True $1470$'
                da_s1 = '$1650$' 
                da_s2 = '$1480$' 
                da_s3 = '$1430$' 
            if b==4 and a=='0,1,2,3,4,5,6,7,8':
                da_d = '\\True $2688$'
                da_s1 = '$2650$' 
                da_s2 = '$3042$' 
                da_s3 = '$3030$' 
            if b==5 and a=='0,1,2,3,4':
                da_d = '\\True $96$'
                da_s1 = '$90$' 
                da_s2 = '$100$' 
                da_s3 = '$140$'
            if b==5 and a=='0,1,2,3,4,5':
                da_d = '\\True $600$'
                da_s1 = '$630$' 
                da_s2 = '$610$' 
                da_s3 = '$640$'
            if b==5 and a=='0,1,2,3,4,5,6':
                da_d = '\\True $2160$'
                da_s1 = '$2130$' 
                da_s2 = '$2180$' 
                da_s3 = '$2140$'
            if b==5 and a=='0,1,2,3,4,5,6,7':
                da_d = '\\True $5880$'
                da_s1 = '$5990$' 
                da_s2 = '$5770$' 
                da_s3 = '$5640$'
            if b==5 and a=='0,1,2,3,4,5,6,7,8':
                da_d = '\\True $13440$'
                da_s1 = '$14440$' 
                da_s2 = '$15440$' 
                da_s3 = '$16440$'
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)
            # Nội dung lời giải
            if b==2 and a=='0,1,2,3,4':
                loigiai=( 'Gọi số cần lập là $\\overline{ab}$, với $a, b$ là các chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                    'Vì $a \\ne 0$ nên có 4 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                    'Ứng với mỗi cách chọn đó, có 4 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                    'Áp dụng quy tắc nhân ta có $4 \\cdot 4 = 16$ số tự nhiên cần lập.'
                    )
            if b==2 and a=='0,1,2,3,4,5':
                loigiai=( 'Gọi số cần lập là $\\overline{ab}$, với $a, b$ là các chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                    'Vì $a \\ne 0$ nên có 5 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                    'Ứng với mỗi cách chọn đó, có 5 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                    'Áp dụng quy tắc nhân ta có $5 \\cdot 5 = 25$ số tự nhiên cần lập.'
                    )
            if b==2 and a=='0,1,2,3,4,5,6':
                loigiai=( 'Gọi số cần lập là $\\overline{ab}$, với $a, b$ là các chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                    'Vì $a \\ne 0$ nên có 6 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                    'Ứng với mỗi cách chọn đó, có 6 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                    'Áp dụng quy tắc nhân ta có $6 \\cdot 6 = 36$ số tự nhiên cần lập.'
                    )
            if b==2 and a=='0,1,2,3,4,5,6,7':
                loigiai=( 'Gọi số cần lập là $\\overline{ab}$, với $a, b$ là các chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                    'Vì $a \\ne 0$ nên có 7 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                    'Ứng với mỗi cách chọn đó, có 7 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                    'Áp dụng quy tắc nhân ta có $7 \\cdot 7 = 49$ số tự nhiên cần lập.'
                    )
            if b==2 and a=='0,1,2,3,4,5,6,7,8':
                loigiai=( 'Gọi số cần lập là $\\overline{ab}$, với $a, b$ là các chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                    'Vì $a \\ne 0$ nên có 8 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                    'Ứng với mỗi cách chọn đó, có 8 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                    'Áp dụng quy tắc nhân ta có $8 \\cdot 8 = 64$ số tự nhiên cần lập.'
                    )

            if b==3 and a=='0,1,2,3,4':
                loigiai=( 'Gọi số cần lập là $\\overline{abc}$, với $a, b, c$ là các chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                    'Vì $a \\ne 0$ nên có 4 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                    'Ứng với mỗi cách chọn đó, có 4 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 3 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                    'Áp dụng quy tắc nhân ta có $4 \\cdot 4 \\cdot 3 = 48$ số tự nhiên cần lập.'
                    )
            if b==3 and a=='0,1,2,3,4,5':
                loigiai=( 'Gọi số cần lập là $\\overline{abc}$, với $a, b, c$ là các chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                    'Vì $a \\ne 0$ nên có 5 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                    'Ứng với mỗi cách chọn đó, có 5 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 4 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                    'Áp dụng quy tắc nhân ta có $5 \\cdot 5 \\cdot 4 = 100$ số tự nhiên cần lập.'
                    )
            if b==3 and a=='0,1,2,3,4,5,6':
                loigiai=( 'Gọi số cần lập là $\\overline{abc}$, với $a, b, c$ là các chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                    'Vì $a \\ne 0$ nên có 6 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                    'Ứng với mỗi cách chọn đó, có 6 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 5 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                    'Áp dụng quy tắc nhân ta có $6 \\cdot 6 \\cdot 5 = 180$ số tự nhiên cần lập.'
                    )
            if b==3 and a=='0,1,2,3,4,5,6,7':
                loigiai=( 'Gọi số cần lập là $\\overline{abc}$, với $a, b, c$ là các chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                    'Vì $a \\ne 0$ nên có 7 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                    'Ứng với mỗi cách chọn đó, có 7 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 6 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                    'Áp dụng quy tắc nhân ta có $7 \\cdot 7 \\cdot 6 = 294$ số tự nhiên cần lập.'
                    )
            if b==3 and a=='0,1,2,3,4,5,6,7,8':
                loigiai=( 'Gọi số cần lập là $\\overline{abc}$, với $a, b, c$ là các chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                    'Vì $a \\ne 0$ nên có 8 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                    'Ứng với mỗi cách chọn đó, có 8 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 7 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                    'Áp dụng quy tắc nhân ta có $8 \\cdot 8 \\cdot 7 = 448$ số tự nhiên cần lập.'
                    )
            if b==4 and a=='0,1,2,3,4':
                loigiai=( 'Gọi số cần lập là $\\overline{abcd}$, với $a, b, c, d$ là các chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                    'Vì $a \\ne 0$ nên có 4 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                    'Ứng với mỗi cách chọn đó, có 4 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 3 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 2 cách chọn chữ số $d$ từ các chữ số còn lại. \\\\'
                    'Áp dụng quy tắc nhân ta có $4 \\cdot 4 \\cdot 3 \\cdot 2 = 96$ số tự nhiên cần lập.'
                    )
            if b==4 and a=='0,1,2,3,4,5':
                loigiai=( 'Gọi số cần lập là $\\overline{abcd}$, với $a, b, c, d$ là các chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                    'Vì $a \\ne 0$ nên có 5 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                    'Ứng với mỗi cách chọn đó, có 5 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 4 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 3 cách chọn chữ số $d$ từ các chữ số còn lại. \\\\'
                    'Áp dụng quy tắc nhân ta có $5 \\cdot 5 \\cdot 4 \\cdot 3 = 300$ số tự nhiên cần lập.'
                    )
            if b==4 and a=='0,1,2,3,4,5,6':
                loigiai=( 'Gọi số cần lập là $\\overline{abcd}$, với $a, b, c, d$ là các chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                    'Vì $a \\ne 0$ nên có 6 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                    'Ứng với mỗi cách chọn đó, có 6 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 5 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 4 cách chọn chữ số $d$ từ các chữ số còn lại. \\\\'
                    'Áp dụng quy tắc nhân ta có $6 \\cdot 6 \\cdot 5 \\cdot 4 = 720$ số tự nhiên cần lập.'
                    )
            if b==4 and a=='0,1,2,3,4,5,6,7':
                loigiai=( 'Gọi số cần lập là $\\overline{abcd}$, với $a, b, c, d$ là các chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                    'Vì $a \\ne 0$ nên có 7 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                    'Ứng với mỗi cách chọn đó, có 7 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 6 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 5 cách chọn chữ số $d$ từ các chữ số còn lại. \\\\'
                    'Áp dụng quy tắc nhân ta có $7 \\cdot 7 \\cdot 6 \\cdot 5 = 1470$ số tự nhiên cần lập.'
                    )
            if b==4 and a=='0,1,2,3,4,5,6,7,8':
                loigiai=( 'Gọi số cần lập là $\\overline{abcd}$, với $a, b, c, d$ là các chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                    'Vì $a \\ne 0$ nên có 8 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                    'Ứng với mỗi cách chọn đó, có 8 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 7 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 6 cách chọn chữ số $d$ từ các chữ số còn lại. \\\\'
                    'Áp dụng quy tắc nhân ta có $8 \\cdot 8 \\cdot 7 \\cdot 6 = 2688$ số tự nhiên cần lập.'
                    )
            if b==5 and a=='0,1,2,3,4':
                loigiai=( 'Gọi số cần lập là $\\overline{abcde}$, với $a, b, c, d, e$ là các chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                    'Vì $a \\ne 0$ nên có 4 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                    'Ứng với mỗi cách chọn đó, có 4 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 3 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 2 cách chọn chữ số $d$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 1 cách chọn chữ số $e$ từ các chữ số còn lại. \\\\'
                    'Áp dụng quy tắc nhân ta có $4 \\cdot 4 \\cdot 3 \\cdot 2 \\cdot 1 = 96$ số tự nhiên cần lập.'
                    )
            if b==5 and a=='0,1,2,3,4,5':
                loigiai=( 'Gọi số cần lập là $\\overline{abcde}$, với $a, b, c, d, e$ là các chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                    'Vì $a \\ne 0$ nên có 5 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                    'Ứng với mỗi cách chọn đó, có 5 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 4 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 3 cách chọn chữ số $d$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 2 cách chọn chữ số $e$ từ các chữ số còn lại. \\\\'
                    'Áp dụng quy tắc nhân ta có $5 \\cdot 5 \\cdot 4 \\cdot 3 \\cdot 2 = 600$ số tự nhiên cần lập.'
                    )
            if b==5 and a=='0,1,2,3,4,5,6':
                loigiai=( 'Gọi số cần lập là $\\overline{abcde}$, với $a, b, c, d, e$ là các chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                    'Vì $a \\ne 0$ nên có 6 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                    'Ứng với mỗi cách chọn đó, có 6 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 5 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 4 cách chọn chữ số $d$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 3 cách chọn chữ số $e$ từ các chữ số còn lại. \\\\'
                    'Áp dụng quy tắc nhân ta có $6 \\cdot 6 \\cdot 5 \\cdot 4 \\cdot 3 = 2160$ số tự nhiên cần lập.'
                    )
            if b==5 and a=='0,1,2,3,4,5,6,7':
                loigiai=( 'Gọi số cần lập là $\\overline{abcde}$, với $a, b, c, d, e$ là các chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                    'Vì $a \\ne 0$ nên có 7 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                    'Ứng với mỗi cách chọn đó, có 7 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 6 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 5 cách chọn chữ số $d$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 4 cách chọn chữ số $e$ từ các chữ số còn lại. \\\\'
                    'Áp dụng quy tắc nhân ta có $7 \\cdot 7 \\cdot 6 \\cdot 5 \\cdot 4 = 5880$ số tự nhiên cần lập.'
                    )
            if b==5 and a=='0,1,2,3,4,5,6,7,8':
                loigiai=( 'Gọi số cần lập là $\\overline{abcde}$, với $a, b, c, d, e$ là các chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                    'Vì $a \\ne 0$ nên có 8 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                    'Ứng với mỗi cách chọn đó, có 8 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 7 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 6 cách chọn chữ số $d$ từ các chữ số còn lại. \\\\'
                    'Ứng với mỗi cách chọn đó, có 5 cách chọn chữ số $e$ từ các chữ số còn lại. \\\\'
                    'Áp dụng quy tắc nhân ta có $8 \\cdot 8 \\cdot 7 \\cdot 6 \\cdot 5 = 13440$ số tự nhiên cần lập.'
                    )
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('++','+').replace('+-','-').replace('--','+').replace('-+','-')
            return content

