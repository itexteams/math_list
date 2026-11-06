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


def bt_dang13_p2_b2_c1_ds12(self):
            # Khai báo biến
            t=symbols('t')
            t1=randint(120,130)
            lisa=[0.001302,0.001301,0.001303,0.001304,0.001305,0.001306]
            a=random.choice(lisa)
            lisb=[0.09029,0.09028,0.09027,0.09026,0.09025,0.09024,0.09023,0.09022,0.09021]
            b=random.choice(lisb)
            lisc=[23.61,23.62,23.63,23.64,23.65,23.66,23.67,23.68,23.69]
            c=random.choice(lisc)
            lisd=[3.081,3.082,3.083,3.084,3.085,3.086,3.087,3.088,3.089]
            d=random.choice(lisd)

            v=a*t**3-b*t**2+c*t-d
            dh=diff(v,t)
            dh2=diff(dh,t)
            pt=Eq(dh2,0)
            giai_pt=solve(pt,t)
            t0="{:.2f}".format(giai_pt[0])

            f0 = "{:.2f}".format(dh.subs(t, 0))
            ft0 = "{:.2f}".format(dh.subs(t, t0))
            ft1 = "{:.2f}".format(dh.subs(t, t1))
            # Nội dung câu hỏi
            noidungcauhoi = ('''Kính viễn vọng không gian Hubble được đưa vào vũ trụ ngày 24/4/1990 bằng tàu con thoi Discoveryzz Vận tốc của tàu con thoi trong sứ mệnh này, từ lúc cất cánh tại thời điểm $t=0$ giây cho đến khi tên lửa đấy được phóng đi tại thời điểm $t=%s$ giây, cho bởi hàm số sau:\\\\
                            $v(t)=%s$ trong đó $v$ được tính bằng feet/s, $1$ feet $=0,3048$ mzz'''                 
                            %(latex(t1),latex(v)
                                ))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Vận tốc của tàu con thoi luôn tăng trong khoảng thời gian từ lúc cất cánh đến khi tên lửa đấy được phóng đi'
            nb_da_1_s = 'Vận tốc của tàu con thoi lúc tăng, lúc giảm trong khoảng thời gian từ lúc cất cánh đến khi tên lửa đấy được phóng đi'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Ta có $a(t)=v'(t)=%s>0, \\forall t \\in (0;%s)$zz \\\\
                            Suy ra vận tốc của tàu con thoi luôn tăng trong khoảng thời gian từ lúc cất cánh đến khi tên lửa đấy được phóng đizz'''
                        %(latex(dh),latex(t1)
                            ))

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
            th_da_1_d = '\\True Gia tốc lớn nhất mà tàu con thoi có thể đạt được trong lúc thực hiện sứ mệnh trên (làm tròn đến hàng phần trăm) là $%s$ feet/s' %(latex(ft1))
            th_da_1_s = 'Gia tốc lớn nhất mà tàu con thoi có thể đạt được trong lúc thực hiện sứ mệnh trên (làm tròn đến hàng phần trăm) là $%s$ feet/s' %(latex(ft0))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''$a'(t)=%s$zz \\\\
                            $a'(t)=0 \\Leftrightarrow %s=0 \\Leftrightarrow t=%s$zz \\\\
                            Bảng biến thiên \\\\
                                \\begin{tikzpicture}
            \\tkzTabInit[espcl=2zz5,lgt=1zz5]
            {$x$/0zz7,$a(t)$/0zz7,$a'(t)$/2zz1}
            {$0$,$%s$,$%s$}
            \\tkzTabLine{,-,0,+}
            \\tkzTabVar{+/$%s$,-/$%s$,+/$%s$}
            \\end{tikzpicture} \\\\
                Dựa vào bảng biến thiên thì gia tốc lớn nhất mà tàu con thoi có thể đạt được trong lúc thực hiện sứ mệnh trên (làm tròn đến hàng phần trăm) là $%s$ feet/szz'''       
                        %(latex(dh2),
                        latex(dh2),latex(t0),
                        latex(t0),latex(t1),
                        latex(f0),latex(ft0),latex(ft1),
                        latex(ft1)
                            ))

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
            vd_da_1_d = '\\True Gia tốc của tàu con thoi giảm trong khoảng thời gian từ lúc cất cánh đến thời điểm $t=%s$ giây' %(latex(int(giai_pt[0])))
            vd_da_1_s = 'Gia tốc của tàu con thoi tăng trong khoảng thời gian từ lúc cất cánh đến thời điểm $t=%s$ giây' %(latex(int(giai_pt[0])))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Dựa vào bảng biến thiên ta thấy gia tốc giảm trong khoảng thời gian từ lúc cất cánh đến thời điểm $t=%s$ giâyzz'''
                        %(latex(int(giai_pt[0]))
                            ))

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
            vdc_da_1_d = '\\True Gia tốc của tàu bắt đầu tăng bắt đầu từ sau thời điểm $t=%s$ giây' %(latex(t0))
            vdc_da_1_s = 'Gia tốc của tàu bắt đầu tăng bắt đầu từ sau thời điểm $t=%s$ giây' %(latex(int(giai_pt[0]+1)))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Dựa vào bảng biến thiên ta thấy gia tốc của tàu bắt đầu tăng bắt đầu từ sau thời điểm $t=%s$ giâyzz'''
                        %(latex(t0)
                            ))

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
                '\\end{ex}\n \\end{minipage} \n\n').replace('.',',').replace('zz','.')
            return content

