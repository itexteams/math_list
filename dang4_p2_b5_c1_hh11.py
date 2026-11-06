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


def bt_dang4_p2_b5_c1_hh11(self):
    # Khai báo và random các đại lượng trong bài toán
    k = random.choice([2, 3, 4, 5])
    k_wrong = random.choice([x for x in [2, 3, 4, 5] if x != k])

    # Nội dung câu hỏi
    noidungcauhoi = ('''Hai đường thẳng phân biệt $a, b$ song song với nhau và đều không cùng phương với phương chiếu. Trên $a$ lấy đoạn $AB$, trên $b$ lấy đoạn $CD$ sao cho $AB = %s CD$. Gọi $a', b', A', B', C', D'$ là các hình chiếu tương ứng.''' % (k))

    ###################################################################### Nhận biết ######################################################
    # Mệnh đề a: Hai đường thẳng a', b' song song hoặc trùng nhau
    nb_da_1_d = '\\True Hai đường thẳng $a\', b\'$ song song hoặc trùng nhau'
    nb_da_1_s = 'Hai đường thẳng $a\', b\'$ luôn luôn cắt nhau'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    list_nb_1 = [nb_da_1]

    loigiai_nb_1 = ('''Phép chiếu song song biến hai đường thẳng song song thành hai đường thẳng song song hoặc trùng nhau, do đó hai đường thẳng $a\', b\'$ song song hoặc trùng nhau.''')

    list_nb_2 = [loigiai_nb_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ###################################################################### Thông hiểu ######################################################
    # Mệnh đề b: Nếu a' và b' trùng nhau thì a và b cũng phải trùng nhau
    th_da_1_s = 'Nếu $a\'$ và $b\'$ trùng nhau thì $a$ và $b$ cũng phải trùng nhau'
    th_da_1_d = '\\True Nếu $a\'$ và $b\'$ trùng nhau thì $a$ và $b$ không nhất thiết phải trùng nhau'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    list_th_1 = [th_da_1]

    loigiai_th_1 = ('''Hai đường thẳng phân biệt $a$ và $b$ song song cùng nằm trong một mặt phẳng chiếu thì hình chiếu $a\'$ và $b\'$ của chúng sẽ trùng nhau. Do đó, $a\'$ và $b\'$ trùng nhau thì $a$ và $b$ vẫn là hai đường thẳng phân biệt, không nhất thiết phải trùng nhau.''')

    list_th_2 = [loigiai_th_1]

    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ###################################################################### Vận dụng ######################################################
    # Mệnh đề c: Ta có A'B' = k C'D'
    vd_da_1_d = '\\True Ta có $A\'B\' = %s C\'D\'$' % (k)
    vd_da_1_s = 'Ta có $A\'B\' = %s C\'D\'$' % (k_wrong)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    list_vd_1 = [vd_da_1]

    loigiai_vd_1 = ('''Phép chiếu song song bảo toàn tỉ số độ dài của hai đoạn thẳng nằm trên hai đường thẳng song song (hoặc cùng nằm trên một đường thẳng). Do $a // b$ và $AB = %s CD$ nên ta có tỉ số $\\dfrac{A\'B\'}{C\'D\'} = \\dfrac{AB}{CD} = %s$, suy ra $A\'B\' = %s C\'D\'$.''' % (k, k, k))

    list_vd_2 = [loigiai_vd_1]

    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ###################################################################### Vận dụng cao ######################################################
    # Mệnh đề d: Nếu a' và b' phân biệt thì a' và b' cắt nhau
    vdc_da_1_s = 'Nếu $a\'$ và $b\'$ phân biệt thì $a\'$ và $b\'$ cắt nhau'
    vdc_da_1_d = '\\True Nếu $a\'$ và $b\'$ phân biệt thì $a\'$ và $b\'$ song song với nhau'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    list_vdc_1 = [vdc_da_1]

    loigiai_vdc_1 = ('''Vì hình chiếu song song của hai đường thẳng song song $a$ và $b$ chỉ có thể song song hoặc trùng nhau, nên nếu $a\'$ và $b\'$ phân biệt thì $a\' // b\'$. Do đó hai đường thẳng này không thể cắt nhau.''')

    list_vdc_2 = [loigiai_vdc_1]

    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    # Lặp đến khi đáp án có từ 1 đến 3 đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    # Gán lại vào list
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
    '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
    '\\choiceTFn \n'
    '{'+str(shuffled_answers_nb[0])+'}\n'
    '{'+str(shuffled_answers_th[0])+'}\n'
    '{'+str(shuffled_answers_vd[0])+'}\n'
    '{'+str(shuffled_answers_vdc[0])+'}\n'
    '\\loigiai{ \n'
    '\\begin{enumEX}[a)]{1} \n'
    '\\item '+str(shuffled_solutions_nb[0])+'\n'
    '\\item '+str(shuffled_solutions_th[0])+'\n'
    '\\item '+str(shuffled_solutions_vd[0])+'\n'
    '\\item '+str(shuffled_solutions_vdc[0])+'\n'
    '\\end{enumEX}} \n'
    '\\end{ex}\n \\end{minipage}\n\n')
    return content

