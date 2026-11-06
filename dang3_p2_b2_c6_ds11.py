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


def bt_dang3_p2_b2_c6_ds11(self):
            # Khai báo biến
            n=randint(38,50)
            a=randint(10,25)
            b=randint(10,25)
            c=randint(3,10)
            while a==b or a==c or b==c or a+b+c+5>=n:
                n=randint(38,50)
                a=randint(10,25)
                b=randint(10,25)
                c=randint(3,10)
            p=nsimplify(a/n)
            q=nsimplify(b/n)
            r=nsimplify(c/n)
            h=p+q-r
            d=1-h
            t1=p-r
            t2=q-r


            # Nội dung câu hỏi
            noidungcauhoi = ('Một khu phố có $%s$ hộ gia đình nuôi chó hoặc nuôi mèo, trong đó có $%s$ hộ nuôi chó, $%s$ hộ nuôi mèo và $%s$ hộ nuôi cả chó và mèo. Chọn ngẫu nhiên một hộ trong khu phố trên.'
                            %(latex(n),latex(a),latex(b),latex(c)))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Xác suất để chọn được hộ nuôi chó là $%s$'%(latex(p))
            nb_da_1_s = 'Xác suất để chọn được hộ nuôi chó là $%s$'%(latex(q))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True Xác suất để chọn được hộ nuôi mèo là $%s$'%(latex(q))
            nb_da_2_s = 'Xác suất để chọn được hộ nuôi mèo là $%s$'%(latex(p))
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]
            nb_da_2=random.choice(list_nb_da_2)

            nb_da_3_d = '\\True Xác suất để chọn được hộ nuôi cả chó và mèo là $%s$'%(latex(r))
            nb_da_3_s = ' Xác suất để chọn được hộ nuôi cả chó và mèo là $%s$'%(latex(p))
            list_nb_da_3=[nb_da_3_d,nb_da_3_s]
            nb_da_3=random.choice(list_nb_da_3)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1, nb_da_2,nb_da_3]

            # Nội dung lời giải
            loigiai_nb_1 = ('Gọi A là biến cố \'\' Chọn được hộ nuôi chó\'\'. \\\\ \n'
                            'Gọi B là biến cố \'\' Chọn được hộ nuôi mèo\'\'. \\\\ \n'
                            'Ta có $P(A)=\\dfrac{%s}{%s}=%s, P(B)=\\dfrac{%s}{%s}=%s, P(AB)=\\dfrac{%s}{%s}=%s$.'%(latex(a),latex(n),latex(p),latex(b),latex(n),latex(q),latex(c),latex(n),latex(r))
                        )
            loigiai_nb_2 =  ('Gọi A là biến cố \'\' Chọn được hộ nuôi chó\'\'. \\\\ \n'
                            'Gọi B là biến cố \'\' Chọn được hộ nuôi mèo\'\'. \\\\ \n'
                            'Ta có $P(A)=\\dfrac{%s}{%s}=%s, P(B)=\\dfrac{%s}{%s}=%s, P(AB)=\\dfrac{%s}{%s}=%s$.'%(latex(a),latex(n),latex(p),latex(b),latex(n),latex(q),latex(c),latex(n),latex(r))
                        )
            loigiai_nb_3 =  ('Gọi A là biến cố \'\' Chọn được hộ nuôi chó\'\'. \\\\ \n'
                            'Gọi B là biến cố \'\' Chọn được hộ nuôi mèo\'\'. \\\\ \n'
                            'Ta có $P(A)=\\dfrac{%s}{%s}=%s, P(B)=\\dfrac{%s}{%s}=%s, P(AB)=\\dfrac{%s}{%s}=%s$.'%(latex(a),latex(n),latex(p),latex(b),latex(n),latex(q),latex(c),latex(n),latex(r))
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1, loigiai_nb_2,loigiai_nb_3]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Xác suất để chọn được hộ nuôi chó hoặc nuôi mèo là $%s$'%(latex(h))
            th_da_1_s = 'Xác suất để chọn được hộ nuôi chó hoặc nuôi mèo $%s$'%(latex(d))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('Xác suất để chọn được hộ nuôi chó hoặc nuôi mèo \\\\ \n'
                            '\\hspace*{1cm} $P(A\\cup B)=P(A)+P(B)-P(AB)=%s+%s-%s=%s$.'%(latex(p),latex(q),latex(r),latex(h))
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
            vd_da_1_d = '\\True Xác suất để chọn được hộ không nuôi cả chó và mèo là $%s$'%(latex(d))
            vd_da_1_s = 'Xác suất để chọn được hộ không nuôi cả chó và mèo là $%s$'%(latex(h))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('Xác suất để chọn được hộ không nuôi cả chó và mèo là \\\\ \n'
                            '\\hspace*{1cm}$P(\\overline{AB})=1-P(A\\cup B)=1-%s=%s$.'%(latex(h),latex(d))
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
            vdc_da_1_d = '\\True Xác suất để chọn hộ nuôi chó và không nuôi mèo là $%s$'%(latex(t1))
            vdc_da_1_s = 'Xác suất để chọn hộ nuôi chó và không nuôi mèo là $%s$'%(latex(p))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = '\\True Xác suất để chọn hộ nuôi mèo và không nuôi chó là $%s$'%(latex(t2))
            vdc_da_2_s = 'Xác suất để chọn hộ nuôi mèo và không nuôi chó là $%s$'%(latex(q))
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]

            vdc_da_2=random.choice(list_vdc_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1, vdc_da_2]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Xác suất để chọn hộ nuôi chó và không nuôi mèo là \\\\ \n'
                            '\\hspace*{1cm}$P(A\\overline{B})=P(A)-P(AB)=%s-%s=%s$.'%(latex(p),latex(r),latex(t1))
                        )
            loigiai_vdc_2 = ('Xác suất để chọn hộ nuôi mèo và không nuôi chó là \\\\ \n'
                            '\\hspace*{1cm}$P(\\overline{A}B)=P(B)-P(AB)=%s-%s=%s$.'%(latex(q),latex(r),latex(t2))
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2]

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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

