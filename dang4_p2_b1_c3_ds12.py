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


def bt_dang4_p2_b1_c3_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                a=randint(3,20)
                b=randint(1,18)
                k=randint(-15,15)
                while a<=b or a-b!=2 or (a+b)%2!=0:
                    a=randint(3,20)
                    b=randint(1,18)
                    k=randint(-15,15)
                kc=k-2
                ke=k-1
                # Nội dung câu hỏi
                noidungcauhoi = '''Cho $F(x)$ là nguyên hàm của hàm số $f(x)=\\dfrac{\\sin %sx+\\sin %sx}{\\sin %sx}$.'''%(latex(a),latex(b),latex(nsimplify((a+b)/2)))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d =  '\\True $f(x)=\\dfrac{2\\sin \\left(\\dfrac{%sx+%sx}{2}\\right)\\cos \\left(\\dfrac{%sx-%sx}{2}\\right)}{\\sin %sx}$'%(latex(a),latex(b),latex(a),latex(b),latex(nsimplify((a+b)/2)))
                nb_da_1_s = '$f(x)=\\dfrac{-2\\sin \\left(\\dfrac{%sx+%sx}{2}\\right)\\cos \\left(\\dfrac{%sx-%sx}{2}\\right)}{\\sin %sx}$'%(latex(a),latex(b),latex(a),latex(b),latex(nsimplify((a+b)/2)))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Ta có $f(x)=\\dfrac{2\\sin \\left(\\dfrac{%sx+%sx}{2}\\right)\\cos \\left(\\dfrac{%sx-%sx}{2}\\right)}{\\sin %sx}=\\dfrac{2\\sin %sx\\cos x}{\\sin %sx}=2\\cos x$.'%(latex(a),latex(b),latex(a),latex(b),latex(nsimplify((a+b)/2)),latex(nsimplify((a+b)/2)),latex(nsimplify((a+b)/2)))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True $f(x)=2\\cos x$'
                th_da_1_s ='$f(x)=2\\sin x$'
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('$f(x)=2\\cos x$.'
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_th_2 = [loigiai_th_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_th = list(zip(list_th_1, list_th_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_th)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ######################################################################## Vận dụng ############################################
                # Các đáp án
                vd_da_1_d = '\\True $F(x)=2\\sin x+\\text{C}$'
                vd_da_1_s = ' $F(x)=2\\cos x+\\text{C}$'
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('Ta có $F(x)=\\displaystyle\\int 2\\cos x \\text{d}x=2\\sin x+\\text{C}.$'
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_vd_2 = [loigiai_vd_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vd = list(zip(list_vd_1, list_vd_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vd)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

                ######################################################################## Vận dụng cao ############################################
                # Các đáp án
                vdc_da_1_d ='\\True Nếu $F\\left(\\dfrac{\\pi}{2}\\right)=%s$ thì $F\\left(\\dfrac{\\pi}{6}\\right)=%s$'%(latex(k),latex(ke))
                vdc_da_1_s = 'Nếu $F\\left(\\dfrac{\\pi}{2}\\right)=%s$ thì $F\\left(\\dfrac{\\pi}{6}\\right)=%s$'%(latex(k),latex(-ke))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Ta có  $F\\left(\\dfrac{\\pi}{2}\\right)=2\\sin \\left(\\dfrac{\\pi}{2}\\right)=2+\\text{C}$ mà theo bài $F\\left(\\dfrac{\\pi}{2}\\right)=%s$ suy ra $\\text{C}=%s-2=%s$.\\\\ \n'
                                'Suy ra $F(x)=2\\cos x+%s$.\\\\ \n'
                                'Vậy $F\\left(\\dfrac{\\pi}{6}\\right)=%s$.'%(latex(k),latex(k),latex(kc),latex(kc),latex(ke))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
            if dang=='2':
                # Khai báo biến
                a=randint(3,20)
                b=randint(1,18)
                k=randint(-15,15)
                while a<=b or a-b!=2 or (a+b)%2!=0:
                    a=randint(3,20)
                    b=randint(1,18)
                    k=randint(-15,15)
                kc=k
                ke=k-2
                # Nội dung câu hỏi
                noidungcauhoi = '''Cho $F(x)$ là nguyên hàm của hàm số $f(x)=\\dfrac{\\cos %sx-\\cos %sx}{\\sin %sx}$.'''%(latex(a),latex(b),latex(nsimplify((a+b)/2)))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d =  '\\True $f(x)=\\dfrac{-2\\sin \\left(\\dfrac{%sx+%sx}{2}\\right)\\sin \\left(\\dfrac{%sx-%sx}{2}\\right)}{\\sin %sx}$'%(latex(a),latex(b),latex(a),latex(b),latex(nsimplify((a+b)/2)))
                nb_da_1_s = '$f(x)=\\dfrac{2\\cos \\left(\\dfrac{%sx+%sx}{2}\\right)\\cos \\left(\\dfrac{%sx-%sx}{2}\\right)}{\\sin %sx}$'%(latex(a),latex(b),latex(a),latex(b),latex(nsimplify((a+b)/2)))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Ta có $f(x)=\\dfrac{-2\\sin \\left(\\dfrac{%sx+%sx}{2}\\right)\\sin \\left(\\dfrac{%sx-%sx}{2}\\right)}{\\sin %sx}=\\dfrac{-2\\sin %sx\\sin x}{\\sin %sx}=-2\\sin x$.'%(latex(a),latex(b),latex(a),latex(b),latex(nsimplify((a+b)/2)),latex(nsimplify((a+b)/2)),latex(nsimplify((a+b)/2)))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True $f(x)=-2\\sin x$'
                th_da_1_s ='$f(x)=2\\sin x$'
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('$f(x)=-2\\sin x$.'
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_th_2 = [loigiai_th_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_th = list(zip(list_th_1, list_th_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_th)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ######################################################################## Vận dụng ############################################
                # Các đáp án
                vd_da_1_d = '\\True $F(x)=2\\cos x+\\text{C}$'
                vd_da_1_s = ' $F(x)=-2\\cos x+\\text{C}$'
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('Ta có $F(x)=\\displaystyle\\int -2\\sin x \\text{d}x=2\\cos x+\\text{C}$.'
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_vd_2 = [loigiai_vd_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vd = list(zip(list_vd_1, list_vd_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vd)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

                ######################################################################## Vận dụng cao ############################################
                # Các đáp án
                vdc_da_1_d ='\\True Nếu $F\\left(\\dfrac{\\pi}{2}\\right)=%s$ thì $F\\left(\\pi\\right)=%s$'%(latex(k),latex(ke))
                vdc_da_1_s = 'Nếu $F\\left(\\dfrac{\\pi}{2}\\right)=%s$ thì $F\\left(\\pi\\right)=%s$'%(latex(k),latex(-ke))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Ta có  $F\\left(\\dfrac{\\pi}{2}\\right)=2\\cos \\left(\\dfrac{\\pi}{2}\\right)=0+\\text{C}$ mà theo bài $F\\left(\\dfrac{\\pi}{2}\\right)=%s$ suy ra $\\text{C}=%s$.\\\\ \n'
                                'Suy ra $F(x)=2\\cos x+%s$.\\\\ \n'
                                'Vậy $F\\left(\\pi\\right)=%s$.'%(latex(k),latex(kc),latex(kc),latex(ke))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
            if dang=='3':
                # Khai báo biến
                a=randint(3,20)
                b=randint(1,18)
                k=randint(-15,15)
                while a<=b or a-b!=2 or (a+b)%2!=0:
                    a=randint(3,20)
                    b=randint(1,18)
                    k=randint(-15,15)
                kc=k+2
                ke=k+2
                # Nội dung câu hỏi
                noidungcauhoi = '''Cho $F(x)$ là nguyên hàm của hàm số $f(x)=\\dfrac{\\cos %sx+\\cos %sx}{\\cos %sx}$.'''%(latex(a),latex(b),latex(nsimplify((a+b)/2)))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d =  '\\True $f(x)=\\dfrac{2\\cos \\left(\\dfrac{%sx+%sx}{2}\\right)\\cos \\left(\\dfrac{%sx-%sx}{2}\\right)}{\\cos %sx}$'%(latex(a),latex(b),latex(a),latex(b),latex(nsimplify((a+b)/2)))
                nb_da_1_s = '$f(x)=\\dfrac{-2\\sin \\left(\\dfrac{%sx+%sx}{2}\\right)\\sin \\left(\\dfrac{%sx-%sx}{2}\\right)}{\\cos %sx}$'%(latex(a),latex(b),latex(a),latex(b),latex(nsimplify((a+b)/2)))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Ta có $f(x)=\\dfrac{2\\cos \\left(\\dfrac{%sx+%sx}{2}\\right)\\cos \\left(\\dfrac{%sx-%sx}{2}\\right)}{\\cos %sx}=\\dfrac{2\\cos %sx\\cos x}{\\cos %sx}=2\\cos x$.'%(latex(a),latex(b),latex(a),latex(b),latex(nsimplify((a+b)/2)),latex(nsimplify((a+b)/2)),latex(nsimplify((a+b)/2)))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True $f(x)=2\\cos x$'
                th_da_1_s ='$f(x)=2\\sin x$'
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('$f(x)=2\\cos x$.'
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_th_2 = [loigiai_th_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_th = list(zip(list_th_1, list_th_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_th)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ######################################################################## Vận dụng ############################################
                # Các đáp án
                vd_da_1_d = '\\True $F(x)=2\\sin x+\\text{C}$'
                vd_da_1_s = ' $F(x)=-2\\sin x+\\text{C}$'
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('Ta có $F(x)=\\displaystyle\\int 2\\cos x \\text{d}x=2\\sin x+\\text{C}.$'
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_vd_2 = [loigiai_vd_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vd = list(zip(list_vd_1, list_vd_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vd)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

                ######################################################################## Vận dụng cao ############################################
                # Các đáp án
                vdc_da_1_d ='\\True Nếu $F\\left(\\pi\\right)=%s$ thì $F\\left(\\dfrac{\\pi}{2}\\right)=%s$'%(latex(k),latex(ke))
                vdc_da_1_s = 'Nếu $F\\left(\\pi\\right)=%s$ thì $F\\left(\\dfrac{\\pi}{2}\\right)=%s$'%(latex(k),latex(-ke))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Ta có  $F\\left(\\pi\\right)=2\\sin \\left(\\pi\\right)=-2+\\text{C}$ mà theo bài $F\\left(\\pi\\right)=%s$ suy ra $\\text{C}=%s+2=%s$.\\\\ \n'
                                'Suy ra $F(x)=2\\sin x+%s$.\\\\ \n'
                                'Vậy $F\\left(\\dfrac{\\pi}{2}\\right)=%s$.'%(latex(k),latex(k),latex(kc),latex(kc),latex(ke))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
            if dang=='4':
                # Khai báo biến
                a=randint(3,20)
                b=randint(1,18)
                k=randint(-15,15)
                while a<=b or a-b!=2 or (a+b)%2!=0:
                    a=randint(3,20)
                    b=randint(1,18)
                    k=randint(-15,15)
                kc=k-2
                ke=k-3
                # Nội dung câu hỏi
                noidungcauhoi = '''Cho $F(x)$ là nguyên hàm của hàm số $f(x)=\\dfrac{\\sin %sx-\\sin %sx}{\\cos %sx}$.'''%(latex(a),latex(b),latex(nsimplify((a+b)/2)))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d =  '\\True $f(x)=\\dfrac{2\\cos \\left(\\dfrac{%sx+%sx}{2}\\right)\\sin \\left(\\dfrac{%sx-%sx}{2}\\right)}{\\cos %sx}$'%(latex(a),latex(b),latex(a),latex(b),latex(nsimplify((a+b)/2)))
                nb_da_1_s = '$f(x)=\\dfrac{2\\sin \\left(\\dfrac{%sx+%sx}{2}\\right)\\cos \\left(\\dfrac{%sx-%sx}{2}\\right)}{\\cos %sx}$'%(latex(a),latex(b),latex(a),latex(b),latex(nsimplify((a+b)/2)))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Ta có $f(x)=\\dfrac{2\\cos \\left(\\dfrac{%sx+%sx}{2}\\right)\\sin \\left(\\dfrac{%sx-%sx}{2}\\right)}{\\cos %sx}=\\dfrac{2\\cos %sx\\sin x}{\\cos %sx}=2\\sin x$.'%(latex(a),latex(b),latex(a),latex(b),latex(nsimplify((a+b)/2)),latex(nsimplify((a+b)/2)),latex(nsimplify((a+b)/2)))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True $f(x)=2\\sin x$'
                th_da_1_s ='$f(x)=2\\cos x$'
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('$f(x)=2\\sin x$.'
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_th_2 = [loigiai_th_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_th = list(zip(list_th_1, list_th_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_th)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ######################################################################## Vận dụng ############################################
                # Các đáp án
                vd_da_1_d = '\\True $F(x)=-2\\cos x+\\text{C}$'
                vd_da_1_s = ' $F(x)=2\\cos x+\\text{C}$'
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('Ta có $F(x)=\\displaystyle\\int 2\\sin x \\text{d}x=-2\\cos x+\\text{C}.$'
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_vd_2 = [loigiai_vd_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vd = list(zip(list_vd_1, list_vd_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vd)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

                ######################################################################## Vận dụng cao ############################################
                # Các đáp án
                vdc_da_1_d ='\\True Nếu $F\\left(\\pi\\right)=%s$ thì $F\\left(\\dfrac{\\pi}{3}\\right)=%s$'%(latex(k),latex(ke))
                vdc_da_1_s = 'Nếu $F\\left(\\pi\\right)=%s$ thì $F\\left(\\dfrac{\\pi}{3}\\right)=%s$'%(latex(k),latex(-ke))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Ta có  $F\\left(\\pi\\right)=-2\\cos \\left(\\pi\\right)=2+\\text{C}$ mà theo bài $F\\left(\\pi\\right)=%s$ suy ra $\\text{C}=%s-2=%s$.\\\\ \n'
                                'Suy ra $F(x)=-2\\cos x+%s$.\\\\ \n'
                                'Vậy $F\\left(\\dfrac{\\pi}{3}\\right)=%s$.'%(latex(k),latex(k),latex(kc),latex(kc),latex(ke))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-','-').replace('--','+')
            return content

