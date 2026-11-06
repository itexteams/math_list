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


def bt_dang1_p2_b2_c1_hh12(self):
            # Khai báo biến
            a=randint(-10,10)
            b=randint(-10,10)
            c=randint(-10,10)
            while a==0 or b==0 or c==0:
                a=randint(-10,10)
                b=randint(-10,10)
                c=randint(-10,10)
            lis=['A','B','C','D','E','F','M','N','P']
            d=random.choice(lis)
            # Nội dung câu hỏi
            noidungcauhoi = '''Trong không gian $Oxyz$ cho điểm $%s(%s;%s;%s)$.'''%(d,latex(a),latex(b),latex(c))

            # Các đáp án
            da_1_d = '\\True Nếu $%s\'$ đối xứng với $%s$ qua mặt phẳng $(Oxy)$ thì $%s\'(%s;%s;%s)$ '%(d,d,d,latex(a),latex(b),latex(-c))
            da_1_s = 'Nếu $%s\'$ đối xứng với $%s$ qua mặt phẳng $(Oxy)$ thì $%s\'(%s;%s;%s)$ '%(d,d,d,latex(-a),latex(-b),latex(c))
            list_da_1=[da_1_d,da_1_s]
            da_1=random.choice(list_da_1)

            da_2_d = '\\True Nếu $%s\'$ đối xứng với $%s$ qua mặt phẳng $(Oxz)$ thì $%s\'(%s;%s;%s)$ '%(d,d,d,latex(a),latex(-b),latex(c))
            da_2_s = 'Nếu $%s\'$ đối xứng với $%s$ qua mặt phẳng $(Oxz)$ thì $%s\'(%s;%s;%s)$ '%(d,d,d,latex(-a),latex(b),latex(-c))
            list_da_2=[da_2_d,da_2_s]
            da_2=random.choice(list_da_2)

            da_3_d = '\\True Nếu $%s\'$ đối xứng với $%s$ qua mặt phẳng $(Oyz)$ thì $%s\'(%s;%s;%s)$ '%(d,d,d,latex(-a),latex(b),latex(c))
            da_3_s = 'Nếu $%s\'$ đối xứng với $%s$ qua mặt phẳng $(Oyz)$ thì $%s\'(%s;%s;%s)$ '%(d,d,d,latex(a),latex(-b),latex(-c))
            list_da_3=[da_3_d,da_3_s]
            da_3=random.choice(list_da_3)

            da_4_d = '\\True Nếu $%s\'$ đối xứng với $%s$ qua trục $Ox$ thì $%s\'(%s;%s;%s)$ '%(d,d,d,latex(a),latex(-b),latex(-c))
            da_4_s = 'Nếu $%s\'$ đối xứng với $%s$ qua trục $Ox$ thì $%s\'(%s;%s;%s)$ '%(d,d,d,latex(-a),latex(b),latex(c))
            list_da_4=[da_4_d,da_4_s]
            da_4=random.choice(list_da_4)

            da_5_d = '\\True Nếu $%s\'$ đối xứng với $%s$ qua trục $Oy$ thì $%s\'(%s;%s;%s)$ '%(d,d,d,latex(-a),latex(b),latex(-c))
            da_5_s = 'Nếu $%s\'$ đối xứng với $%s$ qua trục $Oy$ thì $%s\'(%s;%s;%s)$ '%(d,d,d,latex(a),latex(-b),latex(c))
            list_da_5=[da_5_d,da_5_s]
            da_5=random.choice(list_da_5)

            da_6_d = '\\True Nếu $%s\'$ đối xứng với $%s$ qua trục $Oz$ thì $%s\'(%s;%s;%s)$ '%(d,d,d,latex(-a),latex(-b),latex(c))
            da_6_s = 'Nếu $%s\'$ đối xứng với $%s$ qua trục $Oz$ thì $%s\'(%s;%s;%s)$ '%(d,d,d,latex(a),latex(-b),latex(-c))
            list_da_6=[da_6_d,da_6_s]
            da_6=random.choice(list_da_6)

            da_7_d = '\\True Nếu $%s\'$ đối xứng với $%s$ qua gốc tọa độ $O$ thì $%s\'(%s;%s;%s)$ '%(d,d,d,latex(-a),latex(-b),latex(-c))
            da_7_s = 'Nếu $%s\'$ đối xứng với $%s$ qua gốc tọa độ $O$ thì $%s\'(%s;%s;%s)$ '%(d,d,d,latex(2*a),latex(2*b),latex(2*c))
            list_da_7=[da_7_d,da_7_s]
            da_7=random.choice(list_da_7)

            da_8_d = '\\True Nếu $%s\'$ là hình chiếu của $%s$ lên trục $Ox$ thì $%s\'(%s;%s;%s)$ '%(d,d,d,latex(a),latex(0),latex(0))
            da_8_s = 'Nếu $%s\'$ là hình chiếu của $%s$ lên trục $Ox$ thì $%s\'(%s;%s;%s)$ '%(d,d,d,latex(0),latex(b),latex(c))
            list_da_8=[da_8_d,da_8_s]
            da_8=random.choice(list_da_8)

            da_9_d = '\\True Nếu $%s\'$ là hình chiếu của $%s$ lên trục $Oy$ thì $%s\'(%s;%s;%s)$ '%(d,d,d,latex(0),latex(b),latex(0))
            da_9_s = 'Nếu $%s\'$ là hình chiếu của $%s$ lên trục $Oy$ thì $%s\'(%s;%s;%s)$ '%(d,d,d,latex(0),latex(0),latex(c))
            list_da_9=[da_9_d,da_9_s]
            da_9=random.choice(list_da_9)

            da_10_d = '\\True Nếu $%s\'$ là hình chiếu của $%s$ lên trục $Oz$ thì $%s\'(%s;%s;%s)$ '%(d,d,d,latex(0),latex(0),latex(c))
            da_10_s = 'Nếu $%s\'$ là hình chiếu của $%s$ lên trục $Oz$ thì $%s\'(%s;%s;%s)$ '%(d,d,d,latex(0),latex(0),latex(-c))
            list_da_10=[da_10_d,da_10_s]
            da_10=random.choice(list_da_10)

            da_11_d = '\\True Nếu $%s\'$ là hình chiếu của $%s$ lên mặt phẳng $(Oxy)$ thì $%s\'(%s;%s;%s)$ '%(d,d,d,latex(a),latex(b),latex(0))
            da_11_s = 'Nếu $%s\'$ là hình chiếu của $%s$ lên mặt phẳng $(Oxy)$ thì $%s\'(%s;%s;%s)$ '%(d,d,d,latex(-a),latex(-b),latex(0))
            list_da_11=[da_11_d,da_11_s]
            da_11=random.choice(list_da_11)

            da_12_d = '\\True Nếu $%s\'$ là hình chiếu của $%s$ lên mặt phẳng $(Oxz)$ thì $%s\'(%s;%s;%s)$'%(d,d,d,latex(a),latex(0),latex(c))
            da_12_s = 'Nếu $%s\'$ là hình chiếu của $%s$ lên mặt phẳng $(Oxz)$ thì $%s\'(%s;%s;%s)$ '%(d,d,d,latex(a),latex(b),latex(0))
            list_da_12=[da_12_d,da_12_s]
            da_12=random.choice(list_da_12)

            da_13_d = '\\True Nếu $%s\'$ là hình chiếu của $%s$ lên mặt phẳng $(Oyz)$ thì $%s\'(%s;%s;%s)$ '%(d,d,d,latex(0),latex(b),latex(c))
            da_13_s = 'Nếu $%s\'$ là hình chiếu của $%s$ lên mặt phẳng $(Oyz)$ thì $%s\'(%s;%s;%s)$ '%(d,d,d,latex(a),latex(0),latex(0))
            list_da_13=[da_13_d,da_13_s]
            da_13=random.choice(list_da_13)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_1, da_2, da_3, da_4, da_5, da_6, da_7, da_8, da_9, da_10, da_11, da_12, da_13]

            # Nội dung lời giải
            loigiai_1 = ('Nếu $%s\'$ đối xứng với $%s$ qua mặt phẳng $(Oxy)$ thì $%s\'(%s;%s;%s)$. '%(d,d,d,latex(a),latex(b),latex(-c))
                        )
            loigiai_2 = ('Nếu $%s\'$ đối xứng với $%s$ qua mặt phẳng $(Oxz)$ thì $%s\'(%s;%s;%s)$. '%(d,d,d,latex(a),latex(-b),latex(c))
                        )
            loigiai_3 = (' Nếu $%s\'$ đối xứng với $%s$ qua mặt phẳng $(Oyz)$ thì $%s\'(%s;%s;%s)$. '%(d,d,d,latex(-a),latex(b),latex(c))
                        )
            loigiai_4 = ('Nếu $%s\'$ đối xứng với $%s$ qua trục $Ox$ thì $%s\'(%s;%s;%s)$. '%(d,d,d,latex(a),latex(-b),latex(-c))
                        )
            loigiai_5 = ('Nếu $%s\'$ đối xứng với $%s$ qua trục $Oy$ thì $%s\'(%s;%s;%s)$. '%(d,d,d,latex(-a),latex(b),latex(-c))
                        )
            loigiai_6 = ('Nếu $%s\'$ đối xứng với $%s$ qua trục $Oz$ thì $%s\'(%s;%s;%s)$. '%(d,d,d,latex(-a),latex(-b),latex(c))
                        )
            loigiai_7 = ('Nếu $%s\'$ đối xứng với $%s$ qua gốc tọa độ $O$ thì $%s\'(%s;%s;%s)$. '%(d,d,d,latex(-a),latex(-b),latex(-c))
                        )
            loigiai_8 = ('Nếu $%s\'$ là hình chiếu của $%s$ lên trục $Ox$ thì $%s\'(%s;%s;%s)$. '%(d,d,d,latex(a),latex(0),latex(0))
                        )
            loigiai_9 = ('Nếu $%s\'$ là hình chiếu của $%s$ lên trục $Oy$ thì $%s\'(%s;%s;%s)$. '%(d,d,d,latex(0),latex(b),latex(0))
                        )
            loigiai_10 = ('Nếu $%s\'$ là hình chiếu của $%s$ lên trục $Oz$ thì $%s\'(%s;%s;%s)$. '%(d,d,d,latex(0),latex(0),latex(c))
                        )
            loigiai_11 = ('Nếu $%s\'$ là hình chiếu của $%s$ lên mặt phẳng $(Oxy)$ thì $%s\'(%s;%s;%s)$. '%(d,d,d,latex(a),latex(b),latex(0))
                        )
            loigiai_12 = ('Nếu $%s\'$ là hình chiếu của $%s$ lên mặt phẳng $(Oxz)$ thì $%s\'(%s;%s;%s)$. '%(d,d,d,latex(a),latex(0),latex(c))
                        )
            loigiai_13 = ('Nếu $%s\'$ là hình chiếu của $%s$ lên mặt phẳng $(Oyz)$ thì $%s\'(%s;%s;%s)$. '%(d,d,d,latex(0),latex(b),latex(c))
                        )



            # Đưa các lời giải vào danh sách lời giải
            list_2 = [loigiai_1, loigiai_2, loigiai_3, loigiai_4, loigiai_5, loigiai_6, loigiai_7, loigiai_8, loigiai_9, loigiai_10, loigiai_11, loigiai_12, loigiai_13]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined = list(zip(list_1, list_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers, shuffled_solutions = zip(*combined)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

