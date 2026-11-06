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


def bt_dang2_p2_b4_c1_hh11(self):
            # Khai báo biến
            sa=9
            sb=12
            sc=15
            sm=4
            mn=3
            na=sa-sm-mn

            sm1=Rational(sm*sb,sa)
            sm2=Rational(sm*sc,sa)

            m1n1=Rational(mn*sm1,sm)
            m2n2=Rational(mn*sm2,sm)
            # Nội dung câu hỏi
            noidungcauhoi = ('Cho hình chóp $SABC$ có $SA = %s, SB = %s, SC = %s$. Trên cạnh $SA$ lấy các điểm $M, N$ sao cho $SM = %s, MN = %s, NA = %s$. Vẽ hai mặt phẳng song song với mặt phẳng $(ABC)$ lần lượt qua $M, N$, cắt $SB$ theo thứ tự tại $M\', N\'$ và cắt $SC$ theo thứ tự tại $M\'\', N\'\'$.' 
                            %(latex(sa),latex(sb),latex(sc),
                            latex(sm),latex(mn),latex(na),
                                ))
            hinhve = (   

            '\\begin{center} \n'
                '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]  \n'
                    '\\clip(-1.1314432640583847,-2.8380857417066285) rectangle (4.9861887033297405,5.24828739877185); \n'
                    '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (4.,0.); \n'
                    '\\draw (4.,0.)-- (1.,-2.); \n'
                    '\\draw (1.,-2.)-- (0.,0.); \n'
                    '\\draw (0.,0.)-- (2.,4.); \n'
                    '\\draw (2.,4.)-- (4.,0.); \n'
                    '\\draw (2.,4.)-- (1.,-2.); \n'
                    '\\draw (0.6759259692340722,1.3518519384681444)-- (1.4032165428629688,0.419299257177812); \n'
                    '\\draw (1.4032165428629688,0.419299257177812)-- (3.3505178362509334,1.2989643274981328); \n'
                    '\\draw [dash pattern=on 2pt off 2pt] (3.3505178362509334,1.2989643274981328)-- (0.6759259692340722,1.3518519384681444); \n'
                    '\\draw [dash pattern=on 2pt off 2pt] (1.336577369599961,2.673154739199922)-- (2.6687255910733363,2.662548817853327); \n'
                    '\\draw (2.6687255910733363,2.662548817853327)-- (1.7042593161107764,2.2255558966646585); \n'
                    '\\draw (1.7042593161107764,2.2255558966646585)-- (1.336577369599961,2.673154739199922); \n'
                    '\\draw (1.801848953566159,4.6) node[anchor=north west] {$S$}; \n'
                    '\\draw (-0.5236439757217676,0.4915973161374506) node[anchor=north west] {$A$}; \n'
                    '\\draw (0.6655285449368312,-2) node[anchor=north west] {$B$}; \n'
                    '\\draw (4.087702798832132,0.46517126012281507) node[anchor=north west] {$C$}; \n'
                    '\\draw (0.73159368497342,3.3059722816961368) node[anchor=north west] {$M$}; \n'
                    '\\draw (0.13700742464412063,1.826113144876546) node[anchor=north west] {$N$}; \n'
                    '\\draw (1.6168665614637103,2.3) node[anchor=north west] {$M\'$}; \n'
                    '\\draw (1.3393929733100371,0.6369406242179462) node[anchor=north west] {$N\'$}; \n'
                    '\\draw (2.5,3.3059722816961368) node[anchor=north west] {$M\'\'$}; \n'
                    '\\draw (3.4138383704589264,1.878965256905817) node[anchor=north west] {$N\'\'$}; \n'
                '\\end{tikzpicture}  \n'
            '\\end{center}  \n'

                )

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $SM\' = %s$' %(latex(sm1))
            nb_da_1_s = '$SM\' = %s$' %(latex(sm1+1))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True $SM\'\' = %s$' %(latex(sm2))
            nb_da_2_s = '$SM\'\' = %s$' %(latex(sm2+1))
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]
            nb_da_2=random.choice(list_nb_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1,nb_da_2]

            # Nội dung lời giải
            loigiai_nb_1 = ('Ta có: $(MM\'M\'\') // (NN\'N\'\') // (ABC)$. \\\\ \n'
                            'Áp dụng định lí Thales trong không gian, ta được \\\\ \n'
                            '\\hspace*{1cm} $\\dfrac{SM}{SA} = \\dfrac{SM\'}{SB} = \\dfrac{SM\'\'}{SC} \\Rightarrow \\dfrac{%s}{%s} = \\dfrac{SM\'}{%s} = \\dfrac{SM\'\'}{%s} \\Rightarrow SM\' = %s, SM\'\' = %s$.'
                            %(latex(sm),latex(sa),latex(sb),latex(sc),latex(sm1),latex(sm2))
                        )
            loigiai_nb_2 = ('Ta có: $(MM\'M\'\') // (NN\'N\'\') // (ABC)$. \\\\ \n'
                            'Áp dụng định lí Thales trong không gian, ta được \\\\ \n'
                            '\\hspace*{1cm} $\\dfrac{SM}{SA} = \\dfrac{SM\'}{SB} = \\dfrac{SM\'\'}{SC} \\Rightarrow \\dfrac{%s}{%s} = \\dfrac{SM\'}{%s} = \\dfrac{SM\'\'}{%s} \\Rightarrow SM\' = %s, SM\'\' = %s$.'
                            %(latex(sm),latex(sa),latex(sb),latex(sc),latex(sm1),latex(sm2))
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1,loigiai_nb_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True $M\'N\'=%s$' %(latex(m1n1))
            th_da_1_s = '$M\'N\'=%s$' %(latex(m1n1+1))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True $M\'\'N\'\'=%s$' %(latex(m2n2))
            th_da_2_s = '$M\'\'N\'\'=%s$' %(latex(m2n2+1))
            list_th_da_2=[th_da_2_d,th_da_2_s]
            th_da_2=random.choice(list_th_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1,th_da_2]

            # Nội dung lời giải
            loigiai_th_1 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $\\dfrac{%s}{%s} = \\dfrac{SM}{SB} = \\dfrac{SM\'\'}{SC} \\Rightarrow SM\'\' = %s$. \\\\ \n'
                            'Áp dụng định lí Thales trong không gian, ta được \\\\ \n'
                            '\\hspace*{1cm} $\\dfrac{SM}{MN} = \\dfrac{SM\'}{M\'N\'} = \\dfrac{SM\'\'}{M\'\'N\'\'} \\Rightarrow M\'N\' = %s; M\'\'N\'\' = %s$.'
                            %(latex(sm),latex(sa),latex(sm2),
                            latex(m1n1),latex(m2n2)                  
                        ))
            loigiai_th_2 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $\\dfrac{%s}{%s} = \\dfrac{SM}{SB} = \\dfrac{SM\'\'}{SC} \\Rightarrow SM\'\' = %s$. \\\\ \n'
                            'Áp dụng định lí Thales trong không gian, ta được \\\\ \n'
                            '\\hspace*{1cm} $\\dfrac{SM}{MN} = \\dfrac{SM\'}{M\'N\'} = \\dfrac{SM\'\'}{M\'\'N\'\'} \\Rightarrow M\'N\' = %s; M\'\'N\'\' = %s$.'
                            %(latex(sm),latex(sa),latex(sm2),
                            latex(m1n1),latex(m2n2)                  
                        ))
            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1,loigiai_th_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True $M\'N\' + M\'\'N\'\' = %s$' %(latex(m1n1+m2n2))
            vd_da_1_s = '$M\'N\' + M\'\'N\'\' =  %s$' %(latex(m1n1+m2n2+1))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $M\'N\' + M\'\'N\'\' = %s + %s = %s$.'
                            %(latex(m1n1),latex(m2n2), latex(m1n1+m2n2)            
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
            vdc_da_1_d = '\\True $N\'\'C = %s$' %(latex(sc-sm2-m2n2))
            vdc_da_1_s = '$N\'\'C = %s$' %(latex(sc-sm2-m2n2+1))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = '\\True $N\'B = %s$' %(latex(sb-sm1-m1n1))
            vdc_da_2_s = '$N\'B = %s$' %(latex(sb-sm1-m1n1+1))
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
            vdc_da_2=random.choice(list_vdc_da_2)

            vdc_da_3_d = '\\True $NA= %s$' %(latex(sa-sm-mn))
            vdc_da_3_s = '$NA= %s$' %(latex(sa-sm-mn+1))
            list_vdc_da_3=[vdc_da_3_d,vdc_da_3_s]
            vdc_da_3=random.choice(list_vdc_da_3)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1,vdc_da_2,vdc_da_3]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $N\'\'C = SC - SM\'\' - M\'\'N\'\' = %s - %s - %s = %s$.'
                            %(latex(sc),latex(sm2),latex(m2n2),latex(sc-sm2-m2n2)
                        ))
            loigiai_vdc_2 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $N\'B = SB - SM\' - M\'N\' = %s - %s - %s = %s$.'
                            %(latex(sb),latex(sm1),latex(m1n1),latex(sb-sm1-m1n1)
                        ))
            loigiai_vdc_3 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $NA = SA - SM - MN = %s - %s - %s = %s$.'
                            %(latex(sa),latex(sm),latex(mn),latex(sa-sm-mn)
                        ))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1,loigiai_vdc_2,loigiai_vdc_3]

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
                '\\loigiai{ \n'+hinhve+
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

