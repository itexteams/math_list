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


def bt_dang4_p2_b3_c3_hh10(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến

                x=symbols('x')
                y=symbols('y')
                xa=randint(-9,9)
                ya=randint(-9,9)
                xb=randint(-9,9)
                yb=randint(-9,9)
                xm=randint(-9,9)
                ym=randint(-9,9)
                x0=Rational((xb**2+yb**2-xa**2-ya**2),(2*(xb-xa)))
                bk=sqrt((x0-xa)**2+ya**2)

                while ya==0 or yb==0 or xa==xb or (xm-x0)**2+ym**2<=bk or x0==0:
                    x=symbols('x')
                    y=symbols('y')
                    xa=randint(-9,9)
                    ya=randint(-9,9)
                    xb=randint(-9,9)
                    yb=randint(-9,9)
                    xm=randint(-9,9)
                    ym=randint(-9,9)
                    x0=Rational((xb**2+yb**2-xa**2-ya**2),(2*(xb-xa)))
                    bk=sqrt((x0-xa)**2+ya**2)
                d=(xm-x0)**2+ym**2
                bk=sqrt((x0-xa)**2+ya**2)
                bk1=sqrt((x0-xa)**2+ya**2+1)
                bk2=sqrt((x0-xa)**2+ya**2-1)
                bk3=sqrt((x0-xa)**2+ya**2+2)
                bk4=sqrt((x0-xa)**2+ya**2-2)
                bk5=sqrt((x0-xa)**2+ya**2+3)
                # Nội dung câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $(Oxy)$, đường tròn $(C)$ đi qua hai điểm $A(%s;%s),B(%s;%s)$ và có tâm $I$ thuộc trục hoành.'

                                %(latex(xa),latex(ya),latex(xb),latex(yb))
                                )



                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Tâm $I\\left(%s;0\\right)$'%(latex(x0))
                nb_da_1_s = 'Tâm $I\\left(%s;0\\right)$'%(latex(-x0))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                nb_da_2_d = '\\True Tâm $I\\left(%s;0\\right)$'%(latex(x0))
                nb_da_2_s = 'Tâm $I\\left(%s;0\\right)$'%(latex(x0-1))
                list_nb_da_2=[nb_da_2_d,nb_da_2_s]

                nb_da_2=random.choice(list_nb_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1, nb_da_2]

                # Nội dung lời giải
                loigiai_nb_1 = ('Gọi tâm $I(x;0)\\in Ox$. Ta có $\\vec{AI}=(x-%s;%s);\\vec{BI}=(x-%s;%s)$\\\\ \n'
                        '$IA^2=IB^2 \\Leftrightarrow (x-%s)^2+(%s)^2=(x-%s)^2+(%s)^2 \\Leftrightarrow x=%s$. Khi đó tâm $I\\left(%s;0\\right)$.'
                                %(latex(xa),latex(-ya),latex(xb),latex(-yb),
                                latex(xa),latex(-ya),latex(xb),latex(-yb),latex(x0),latex(x0),)
                            )
                loigiai_nb_2 = ('Gọi tâm $I(x;0)\\in Ox$. Ta có $\\vec{AI}=(x-%s;%s);\\vec{BI}=(x-%s;%s)$\\\\ \n'
                        '$IA^2=IB^2 \\Leftrightarrow (x-%s)^2+(%s)^2=(x-%s)^2+(%s)^2 \\Leftrightarrow x=%s$. Khi đó tâm $I\\left(%s;0\\right)$.'
                                %(latex(xa),latex(-ya),latex(xb),latex(-yb),
                                latex(xa),latex(-ya),latex(xb),latex(-yb),latex(x0),latex(x0),)
                            )
                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1, loigiai_nb_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True Bán kính đường tròn $(C)$ là $R=%s$ '%(latex(bk))
                th_da_1_s = 'Bán kính đường tròn $(C)$ là $R=%s$ '%(latex(bk2))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                th_da_2_d = '\\True Bán kính đường tròn $(C)$ là $R=%s$ '%(latex(bk))
                th_da_2_s = 'Bán kính đường tròn $(C)$ là $R=%s$ '%(latex(bk1))
                list_th_da_2=[th_da_2_d,th_da_2_s]

                th_da_2=random.choice(list_th_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1, th_da_2]

                # Nội dung lời giải
                loigiai_th_1 = ('Bán kính đường tròn $(C)$ là $R=AI=\\sqrt{\\left(%s-%s\\right)^2+(%s)^2}=%s$. '
                                %(latex(x0),latex(xa),latex(-ya),latex(bk),)
                            )
                loigiai_th_2 = ('Bán kính đường tròn $(C)$ là $R=AI=\\sqrt{\\left(%s-%s\\right)^2+(%s)^2}=%s$. '
                                %(latex(x0),latex(xa),latex(-ya),latex(bk),)
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_th_2 = [loigiai_th_1, loigiai_th_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_th = list(zip(list_th_1, list_th_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_th)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ######################################################################## Vận dụng ############################################
                # Các đáp án
                vd_da_1_d = '\\True Phương trình đường tròn $(C)$ là $\\left(x-%s\\right)^2+y^2=%s$'%(latex(x0),latex(bk**2))
                vd_da_1_s = 'Phương trình đường tròn $(C)$ là $\\left(x-%s\\right)^2+y^2=%s$'%(latex(-x0),latex(bk**2))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                vd_da_2_d = '\\True Phương trình đường tròn $(C)$ là $\\left(x-%s\\right)^2+y^2=%s$'%(latex(x0),latex(bk**2))
                vd_da_2_s = 'Phương trình đường tròn $(C)$ là $\\left(x-%s\\right)^2+y^2=%s$'%(latex(-x0),latex(bk2**2))
                list_vd_da_2=[vd_da_2_d,vd_da_2_s]

                vd_da_2=random.choice(list_vd_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1, vd_da_2]

                # Nội dung lời giải
                loigiai_vd_1 = ('Phương trình đường tròn $(C)$ là $\\left(x-%s\\right)^2+y^2=%s$.'%(latex(x0),latex(bk**2))
                            )
                loigiai_vd_2 = ('Phương trình đường tròn $(C)$ là $\\left(x-%s\\right)^2+y^2=%s$.'%(latex(x0),latex(bk**2))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_vd_2 = [loigiai_vd_1, loigiai_vd_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vd = list(zip(list_vd_1, list_vd_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vd)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

                ######################################################################## Vận dụng cao ############################################
                # Các đáp án
                vdc_da_1_d = '\\True Điểm $M(%s;%s)$ nằm ngoài đường tròn $(C)$'%(latex(xm),latex(ym))
                vdc_da_1_s = 'Điểm $M(%s;%s)$ nằm trong đường tròn $(C)$'%(latex(xm),latex(ym))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '\\True Điểm $M(%s;%s)$ nằm ngoài đường tròn $(C)$'%(latex(xm),latex(ym))
                vdc_da_2_s = 'Điểm $M(%s;%s)$ nằm trên đường tròn $(C)$'%(latex(xm),latex(ym))
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]

                vdc_da_2=random.choice(list_vdc_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1, vdc_da_2]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Với $M(%s;%s)$, ta có $IM=\\sqrt{\\left(%s-%s\\right)^2+(%s)^2}=%s>R \\Rightarrow $ điểm $M$ nằm ngoài đường tròn $C$.'

                                %(latex(xm),latex(ym),latex(xm),latex(x0),latex(ym),latex(sqrt(d)),)
                            )
                loigiai_vdc_2 = ('Với $M(%s;%s)$, ta có $IM=\\sqrt{\\left(%s-%s\\right)^2+(%s)^2}=%s>R \\Rightarrow $ điểm $M$ nằm ngoài đường tròn $C$.'

                                %(latex(xm),latex(ym),latex(xm),latex(x0),latex(ym),latex(sqrt(d)),)
                            )
                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)


            if dang=='2':
                # Khai báo biến

                x=symbols('x')
                y=symbols('y')
                xa=randint(-9,9)
                ya=randint(-9,9)
                xb=randint(-9,9)
                yb=randint(-9,9)
                xm=randint(-9,9)
                ym=randint(-9,9)
                x0=Rational((xb**2+yb**2-xa**2-ya**2),(2*(xb-xa)))
                bk=sqrt((x0-xa)**2+ya**2)

                while ya==0 or yb==0 or xa==xb or (xm-x0)**2+ym**2>=bk or x0==0:
                    x=symbols('x')
                    y=symbols('y')
                    xa=randint(-9,9)
                    ya=randint(-9,9)
                    xb=randint(-9,9)
                    yb=randint(-9,9)
                    xm=randint(-9,9)
                    ym=randint(-9,9)
                    x0=Rational((xb**2+yb**2-xa**2-ya**2),(2*(xb-xa)))
                    bk=sqrt((x0-xa)**2+ya**2)
                d=(xm-x0)**2+ym**2
                bk=sqrt((x0-xa)**2+ya**2)
                bk1=sqrt((x0-xa)**2+ya**2+1)
                bk2=sqrt((x0-xa)**2+ya**2-1)
                bk3=sqrt((x0-xa)**2+ya**2+2)
                bk4=sqrt((x0-xa)**2+ya**2-2)
                bk5=sqrt((x0-xa)**2+ya**2+3)
                # Nội dung câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $(Oxy)$, đường tròn $(C)$ đi qua hai điểm $A(%s;%s),B(%s;%s)$ và có tâm $I$ thuộc trục hoành.'

                                %(latex(xa),latex(ya),latex(xb),latex(yb))
                                )



                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Tâm $I\\left(%s;0\\right)$'%(latex(x0))
                nb_da_1_s = 'Tâm $I\\left(%s;0\\right)$'%(latex(-x0))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                nb_da_2_d = '\\True Tâm $I\\left(%s;0\\right)$'%(latex(x0))
                nb_da_2_s = 'Tâm $I\\left(%s;0\\right)$'%(latex(x0-1))
                list_nb_da_2=[nb_da_2_d,nb_da_2_s]

                nb_da_2=random.choice(list_nb_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1, nb_da_2]

                # Nội dung lời giải
                loigiai_nb_1 = ('Gọi tâm $I(x;0)\\in Ox$. Ta có $\\vec{AI}=(x-%s;%s);\\vec{BI}=(x-%s;%s)$\\\\ \n'
                        '$IA^2=IB^2 \\Leftrightarrow (x-%s)^2+(%s)^2=(x-%s)^2+(%s)^2 \\Leftrightarrow x=%s$. Khi đó tâm $I\\left(%s;0\\right)$.'
                                %(latex(xa),latex(-ya),latex(xb),latex(-yb),
                                latex(xa),latex(-ya),latex(xb),latex(-yb),latex(x0),latex(x0),)
                            )
                loigiai_nb_2 = ('Gọi tâm $I(x;0)\\in Ox$. Ta có $\\vec{AI}=(x-%s;%s);\\vec{BI}=(x-%s;%s)$\\\\ \n'
                        '$IA^2=IB^2 \\Leftrightarrow (x-%s)^2+(%s)^2=(x-%s)^2+(%s)^2 \\Leftrightarrow x=%s$. Khi đó tâm $I\\left(%s;0\\right)$.'
                                %(latex(xa),latex(-ya),latex(xb),latex(-yb),
                                latex(xa),latex(-ya),latex(xb),latex(-yb),latex(x0),latex(x0),)
                            )
                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1, loigiai_nb_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True Bán kính đường tròn $(C)$ là $R=%s$ '%(latex(bk))
                th_da_1_s = 'Bán kính đường tròn $(C)$ là $R=%s$ '%(latex(bk2))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                th_da_2_d = '\\True Bán kính đường tròn $(C)$ là $R=%s$ '%(latex(bk))
                th_da_2_s = 'Bán kính đường tròn $(C)$ là $R=%s$ '%(latex(bk1))
                list_th_da_2=[th_da_2_d,th_da_2_s]

                th_da_2=random.choice(list_th_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1, th_da_2]

                # Nội dung lời giải
                loigiai_th_1 = ('Bán kính đường tròn $(C)$ là $R=AI=\\sqrt{\\left(%s-%s\\right)^2+(%s)^2}=%s$. '
                                %(latex(x0),latex(xa),latex(-ya),latex(bk),)
                            )
                loigiai_th_2 = ('Bán kính đường tròn $(C)$ là $R=AI=\\sqrt{\\left(%s-%s\\right)^2+(%s)^2}=%s$. '
                                %(latex(x0),latex(xa),latex(-ya),latex(bk),)
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_th_2 = [loigiai_th_1, loigiai_th_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_th = list(zip(list_th_1, list_th_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_th)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ######################################################################## Vận dụng ############################################
                # Các đáp án
                vd_da_1_d = '\\True Phương trình đường tròn $(C)$ là $\\left(x-%s\\right)^2+y^2=%s$'%(latex(x0),latex(bk**2))
                vd_da_1_s = 'Phương trình đường tròn $(C)$ là $\\left(x-%s\\right)^2+y^2=%s$'%(latex(x0),latex(bk1**2))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                vd_da_2_d = '\\True Phương trình đường tròn $(C)$ là $\\left(x-%s\\right)^2+y^2=%s$'%(latex(x0),latex(bk**2))
                vd_da_2_s = 'Phương trình đường tròn $(C)$ là $\\left(x-%s\\right)^2+y^2=%s$'%(latex(-x0),latex(bk**2))
                list_vd_da_2=[vd_da_2_d,vd_da_2_s]

                vd_da_2=random.choice(list_vd_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1, vd_da_2]

                # Nội dung lời giải
                loigiai_vd_1 = ('Phương trình đường tròn $(C)$ là $\\left(x-%s\\right)^2+y^2=%s$.'%(latex(x0),latex(bk**2))
                            )
                loigiai_vd_2 = ('Phương trình đường tròn $(C)$ là $\\left(x-%s\\right)^2+y^2=%s$.'%(latex(x0),latex(bk**2))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_vd_2 = [loigiai_vd_1, loigiai_vd_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vd = list(zip(list_vd_1, list_vd_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vd)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

                ######################################################################## Vận dụng cao ############################################
                # Các đáp án
                vdc_da_1_d = '\\True Điểm $M(%s;%s)$ nằm trong đường tròn $(C)$'%(latex(xm),latex(ym))
                vdc_da_1_s = 'Điểm $M(%s;%s)$ nằm ngoài đường tròn $(C)$'%(latex(xm),latex(ym))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '\\True Điểm $M(%s;%s)$ nằm trong đường tròn $(C)$'%(latex(xm),latex(ym))
                vdc_da_2_s = 'Điểm $M(%s;%s)$ nằm trên đường tròn $(C)$'%(latex(xm),latex(ym))
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]

                vdc_da_2=random.choice(list_vdc_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1, vdc_da_2]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Với $M(%s;%s)$, ta có $IM=\\sqrt{\\left(%s-%s\\right)^2+(%s)^2}=%s<R \\Rightarrow $ điểm $M$ nằm trong đường tròn $C$.'

                                %(latex(xm),latex(ym),latex(xm),latex(x0),latex(ym),latex(sqrt(d)),)
                            )
                loigiai_vdc_2 = ('Với $M(%s;%s)$, ta có $IM=\\sqrt{\\left(%s-%s\\right)^2+(%s)^2}=%s<R \\Rightarrow $ điểm $M$ nằm trong đường tròn $C$.'

                                %(latex(xm),latex(ym),latex(xm),latex(x0),latex(ym),latex(sqrt(d)),)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '+')
            return content   

